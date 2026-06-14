# Android UI Tests

Проект автоматизации тестирования Android-приложения с использованием Appium и Pytest.

## Возможности проекта

* Автоматизированное тестирование Android-приложения;
* Проверка отображения элементов интерфейса;
* Проверка навигации между экранами;
* Проверка работы текстовых полей ввода;
* Проверка цветов элементов интерфейса;
* Формирование Allure-отчетов;
* Автоматическое создание скриншотов при падении тестов;
* Запуск тестов локально и в GitHub Actions.

## Предварительные требования для локального запуска

Перед запуском тестов необходимо установить и настроить:

### 1. Python

Рекомендуемая версия:

```bash
Python 3.13
```

### 2. Appium

Установить Appium:

```bash
npm install -g appium
```

Установить драйвер UiAutomator2:

```bash
appium driver install uiautomator2
```

Проверить установленные драйверы:

```bash
appium driver list --installed
```

### 3. Android SDK

Необходимо установить Android Studio или Android SDK и настроить переменные окружения:

* ANDROID_HOME
* ANDROID_SDK_ROOT

Также должен быть доступен ADB:

```bash
adb devices
```

### 4. Android Emulator

Необходимо создать и запустить Android Emulator.

Например:

* Pixel 6
* Android API 35

Проверить подключение эмулятора:

```bash
adb devices
```

В списке устройств должен отображаться запущенный эмулятор.

### 5. APK приложения

Debug APK должен находиться по пути:

```text
app/app-debug.apk
```

## Установка зависимостей

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать его:

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Локальный запуск тестов

### Запустить Appium

```bash
appium
```

### Запустить все тесты

```bash
pytest
```

### Запустить группу тестов

Например, тесты главного экрана:

```bash
pytest -m home_screen
```

### Запуск с логированием

```bash
LOG_LEVEL=DEBUG pytest
```

## Allure-отчеты

Запуск тестов с генерацией результатов:

```bash
pytest --alluredir=allure-results
```

Просмотр отчета:

```bash
allure serve allure-results
```

## Скриншоты при падении тестов

При падении теста автоматически сохраняется скриншот устройства.

Скриншоты сохраняются в директорию:

```text
screenshots/
```

При использовании Allure скриншоты также прикладываются к отчету.

## CI/CD

В проекте настроен запуск тестов в GitHub Actions.

Workflow выполняет:

* запуск Android Emulator;
* запуск Appium Server;
* установку APK;
* выполнение тестов;
* сохранение Allure Results;
* сохранение логов Appium;
* сохранение скриншотов упавших тестов.

## Автор

Roman Bobkov
