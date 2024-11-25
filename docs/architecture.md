HarvestLink/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── .env
├── docs/
│   └── arquitetura.md
├── scripts/
│   └── start.sh
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logging.conf
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── presentation/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   └── cli/
│   │       ├── __init__.py
│   │       └── commands.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   └── device.py
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── device_repository.py
│   │   │   └── network_service.py
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       └── manage_device.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── device_repository_impl.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── network_service_impl.py
│   │   └── persistence/
│   │       ├── __init__.py
│   │       ├── database.py
│   │       ├── models.py
│   │       └── migrations/
│   │           └── versions/
│   └── shared/
│       ├── __init__.py
│       ├── utils.py
│       └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_manage_device.py
│   └── integration/
│       ├── __init__.py
│       └── test_api.py
├── deployment/
│   ├── kubernetes/
│   │   └── deployment.yaml
│   └── ansible/
│       └── playbook.yml
