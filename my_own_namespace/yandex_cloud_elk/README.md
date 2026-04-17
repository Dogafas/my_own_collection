# my_own_namespace.yandex_cloud_elk

Учебная Ansible‑коллекция, демонстрирующая создание собственного модуля и роли.  
Коллекция включает:

- Python‑модуль `my_own_module`
- Роль `create_file`, использующую этот модуль
- Тестовый playbook для проверки идемпотентности
- Пример playbook для роли

---

## Структура коллекции
```
yandex_cloud_elk/
├── galaxy.yml
├── README.md
├── test_idempotent.yml
├── playbooks/
│   └── create_file.yml
├── plugins/
│   └── modules/
│       ├── init.py
│       └── my_own_module.py
├── roles/
│   └── create_file/
│       ├── defaults/main.yml
│       ├── handlers/main.yml
│       ├── meta/main.yml
│       ├── tasks/main.yml
│       ├── vars/main.yml
│       ├── tests/
│       │   ├── inventory
│       │   └── test.yml
│       └── README.md
└── meta/runtime.yml
```

---

## Установка коллекции

Собрать архив:
```
ansible-galaxy collection build
```

Установить из архива:
```
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz --force
```

---

## Использование модуля

Пример playbook:

```yaml
- name: Test custom module
hosts: localhost
tasks:

name: Create file using custom module
my_own_namespace.yandex_cloud_elk.my_own_module:
path: "/tmp/test_file.txt"
content: "Hello from custom module"
```

---

## Использование роли

- name: Create file using collection role
  hosts: localhost
  roles:
    - my_own_namespace.yandex_cloud_elk.create_file


---

## Проверка идемпотентности модуля

```bash
ansible-playbook test_idempotent.yml
ansible-playbook test_idempotent.yml
```

Ожидаемый результат:

- первый запуск → changed=1  
- второй запуск → changed=0  

---

## Проверка роли

```bash
ansible-playbook playbooks/create_file.yml
ansible-playbook playbooks/create_file.yml
```

Ожидаемый результат:

- первый запуск → changed=1  
- второй запуск → changed=0  

---
Автор: ChipGuru



