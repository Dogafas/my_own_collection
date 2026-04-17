# Роль `create_file`

Роль предназначена для создания текстового файла на целевом хосте с использованием пользовательского модуля `my_own_module`, входящего в коллекцию `my_own_namespace.yandex_cloud_elk`.

Роль является высокоуровневой оберткой над модулем и предоставляет значения по умолчанию, определённые в `defaults/main.yml`.

---

## Требования

Роль является частью коллекции:

```
my_own_namespace.yandex_cloud_elk
```

Перед использованием необходимо установить коллекцию:

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

---

## Переменные роли

Значения по умолчанию определены в `defaults/main.yml`:

```yaml
path: /tmp/testfile.txt
content: "Hello from my module"
```

Описание переменных:

| Переменная | Тип    | Обязательная | Описание |
|-----------|--------|--------------|----------|
| `path`    | string | Да           | Абсолютный путь к создаваемому файлу |
| `content` | string | Да           | Содержимое, которое будет записано в файл |

---

## Пример использования роли

Минимальный playbook:

```yaml
---
- name: Create file using role
  hosts: localhost
  gather_facts: false

  roles:
    - my_own_namespace.yandex_cloud_elk.create_file
```

---

## Пример с переопределением переменных

```yaml
---
- name: Create custom file
  hosts: localhost
  gather_facts: false

  roles:
    - role: my_own_namespace.yandex_cloud_elk.create_file
      vars:
        path: /tmp/custom_file.txt
        content: "Custom content from playbook"
```

---

## Что делает роль

1. Вызывает модуль `my_own_module`.
2. Передает ему параметры `path` и `content`.
3. Обеспечивает идемпотентность:
   - если файл существует и содержимое совпадает, изменений не происходит;
   - если файл отсутствует или содержимое отличается, файл создается или перезаписывается.

---

## Структура роли

```
roles/create_file/
├── defaults/
│   └── main.yml
├── tasks/
│   └── main.yml
├── handlers/
├── meta/
├── templates/
├── vars/
└── README.md
```

---

## Лицензия

GPL-2.0-or-later
