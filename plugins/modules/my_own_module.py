#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import os

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Create a text file with specified content
version_added: "1.0.0"
description: Creates a text file on the remote host with given content.
options:
    path:
        description: Path to the file that should be created.
        required: true
        type: str
    content:
        description: Content to write into the file.
        required: true
        type: str
author:
    - Cameron
'''

EXAMPLES = r'''
- name: Create file with content
  my_namespace.my_collection.my_own_module:
    path: /tmp/testfile.txt
    content: "Hello world!"
'''

RETURN = r'''
changed:
    description: Whether the file was created or modified.
    type: bool
    returned: always
path:
    description: Path to the file.
    type: str
    returned: always
'''

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path

    # Если check_mode — просто сообщаем, что бы произошло
    if module.check_mode:
        if not os.path.exists(path):
            result['changed'] = True
        else:
            with open(path, 'r') as f:
                existing = f.read()
            if existing != content:
                result['changed'] = True
        module.exit_json(**result)

    # Проверяем, существует ли файл и совпадает ли содержимое
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing = f.read()
        if existing == content:
            module.exit_json(**result)

    # Создаём или перезаписываем файл
    try:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True
    except Exception as e:
        module.fail_json(msg=f"Failed to write file: {e}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
