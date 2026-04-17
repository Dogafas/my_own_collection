# Ansible Collection — `my_own_namespace.yandex_cloud_elk`

Коллекция демонстрирует создание пользовательского Ansible‑модуля на Python и его интеграцию в роль.  
Основная задача — создание текстового файла на целевом хосте с указанным содержимым.

Коллекция включает:

- **Модуль `my_own_module`** — низкоуровневый Python‑модуль, создающий файл по заданному пути.
- **Роль `create_file`** — высокоуровневая обёртка над модулем, предоставляющая значения по умолчанию.

---

## Установка коллекции

### 1. Сборка архива коллекции

В корневой директории коллекции выполните:

```bash
ansible-galaxy collection build
```

Будет создан файл вида:

```
my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

### 2. Установка из локального архива

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

Коллекция будет установлена в:

```
~/.ansible/collections/ansible_collections/my_own_namespace/yandex_cloud_elk/
```

---

## Использование коллекции

### 1. Использование роли (рекомендуемый способ)

Файл: `playbooks/create_file.yml`

```yaml
---
- name: Create file using collection role
  hosts: localhost
  gather_facts: false

  roles:
    - my_own_namespace.yandex_cloud_elk.create_file
```

Роль использует значения по умолчанию из `defaults/main.yml`:

```yaml
path: /tmp/testfile.txt
content: "Hello from my module"
```

---

### 2. Прямой вызов модуля

```yaml
---
- name: Create file directly via module
  hosts: localhost
  gather_facts: false

  tasks:
    - name: Create file using custom module
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/example_direct.txt
        content: "Created directly via module"
```

---

## Параметры модуля `my_own_module`

| Параметр | Тип    | Обязательный | Описание |
|---------|--------|--------------|----------|
| `path`  | string | Да           | Абсолютный путь к создаваемому файлу |
| `content` | string | Да         | Содержимое, которое будет записано в файл |

### Особенности

- Модуль **идемпотентен**:  
  если файл существует и содержимое совпадает — изменений не происходит.
- Поддерживает **check_mode**.

---

## Структура коллекции

```
my_own_namespace/
└── yandex_cloud_elk/
    ├── galaxy.yml
    ├── README.md
    ├── meta/
    │   └── runtime.yml
    ├── plugins/
    │   └── modules/
    │       ├── __init__.py
    │       └── my_own_module.py
    ├── roles/
    │   └── create_file/
    │       ├── defaults/
    │       │   └── main.yml
    │       ├── tasks/
    │       │   └── main.yml
    │       ├── handlers/
    │       ├── meta/
    │       ├── templates/
    │       ├── vars/
    │       └── README.md
    ├── playbooks/
    │   └── create_file.yml
    └── test_idempotent.yml
```

---

## Лицензия

Коллекция распространяется под лицензией **GPL‑2.0‑or‑later**.

