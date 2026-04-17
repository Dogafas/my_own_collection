# My Own Ansible Collection

Этот репозиторий содержит учебную Ansible‑коллекцию `my_own_namespace.yandex_cloud_elk`, разработанную в рамках практического задания.  
Коллекция включает собственный модуль, роль, тестовые playbook’и и примеры использования.

## Структура репозитория

```
my_own_collection/
└── my_own_namespace/
├── image.png
├── image-1.png
├── image-2.png
├── screen.md
├── playbooks/
│   └── create_file.yml
└── yandex_cloud_elk/
├── galaxy.yml
├── README.md
├── meta/
├── plugins/
├── roles/
├── playbooks/
└── test_idempotent.yml
```

## Сборка коллекции

Перейдите в каталог коллекции:

```bash
cd my_own_namespace/yandex_cloud_elk
ansible-galaxy collection build
```

Будет создан архив вида:

```bash
my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## Установка коллекции

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz --force
```


## Проверка работы модуля

```bash
ansible-playbook test_idempotent.yml
ansible-playbook test_idempotent.yml
```


Ожидаемое поведение:

- первый запуск: changed=1  
- второй запуск: changed=0  

## Проверка работы роли

```bash
ansible-playbook playbooks/create_file.yml
ansible-playbook playbooks/create_file.yml
```

Ожидаемое поведение:

- первый запуск: changed=1  
- второй запуск: changed=0  

## Тегирование

Коллекция помечена тегом:

```bash
1.0.0
```


Тег указывает на актуальное состояние репозитория.

## Автор

ByteBard

