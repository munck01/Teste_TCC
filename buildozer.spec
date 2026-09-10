# =============================================================================
# Buildozer configuration
# Kivy Android APK
# =============================================================================

[app]

# -----------------------------------------------------------------------------
# Aplicação
# -----------------------------------------------------------------------------

title = Teste Acelerometro

package.name = teste_acelerometro

package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1

# -----------------------------------------------------------------------------
# Dependências Python / Kivy
# -----------------------------------------------------------------------------

requirements = python3,kivy,plyer

# -----------------------------------------------------------------------------
# Interface
# -----------------------------------------------------------------------------

orientation = portrait

fullscreen = 0

# -----------------------------------------------------------------------------
# Android
# -----------------------------------------------------------------------------

# API alvo
android.api = 33

# API mínima
android.minapi = 21

# NDK compatível com API 33 / Python-for-Android
android.ndk = 25b

# Arquiteturas
android.archs = arm64-v8a,armeabi-v7a

# Aceitar automaticamente as licenças do SDK
android.accept_sdk_license = True

# Manter backup do Android
android.allow_backup = True

# -----------------------------------------------------------------------------
# Bootstrap
# -----------------------------------------------------------------------------

p4a.bootstrap = sdl2

# -----------------------------------------------------------------------------
# Python-for-Android
# -----------------------------------------------------------------------------

# Python-for-Android
# p4a.url = https://github.com/kivy/python-for-android.git
# Comente ou apague a linha abaixo para usar o branch padrão/recente
# p4a.branch = release-2024.01

# Python utilizado dentro do APK
p4a.extra_args = --python-version=3.10

# -----------------------------------------------------------------------------
# Permissões
# -----------------------------------------------------------------------------

# O acelerômetro normalmente não precisa de permissão perigosa.
# Se posteriormente usar outros sensores/recursos, podemos adicionar aqui.
android.permissions =

# -----------------------------------------------------------------------------
# Ícone / Splash
# -----------------------------------------------------------------------------

# Descomente somente se os arquivos existirem.
#
# icon.filename = %(source.dir)s/data/icon.png
#
# presplash.filename = %(source.dir)s/data/presplash.png

# -----------------------------------------------------------------------------
# Java / Android
# -----------------------------------------------------------------------------

# Entry point padrão do Kivy.
# Não precisamos sobrescrever o padrão.

# android.entrypoint = org.kivy.android.PythonActivity

# -----------------------------------------------------------------------------
# Recursos
# -----------------------------------------------------------------------------

# Nenhum recurso Android adicional neste momento.

# android.add_assets =
# android.add_resources =
# android.add_src =
# android.add_aars =
# android.add_jars =

# -----------------------------------------------------------------------------
# Gradle
# -----------------------------------------------------------------------------

# Não adicionar dependências Gradle extras sem necessidade.

# android.gradle_dependencies =
# android.enable_androidx = True

# -----------------------------------------------------------------------------
# Android Manifest
# -----------------------------------------------------------------------------

# Não precisamos de alterações no Manifest para o acelerômetro básico.

# android.extra_manifest_xml =
# android.extra_manifest_application_arguments =

# -----------------------------------------------------------------------------
# Logs Android
# -----------------------------------------------------------------------------

# Mantemos o log normal para facilitar diagnóstico posteriormente.

# android.logcat_filters = *:S python:D

# -----------------------------------------------------------------------------
# Outros
# -----------------------------------------------------------------------------

android.wakelock = False

android.copy_libs = 1

# -----------------------------------------------------------------------------
# iOS
# -----------------------------------------------------------------------------

# Não utilizado neste workflow, mas mantido para compatibilidade
# com o template original.

ios.kivy_ios_url = https://github.com/kivy/kivy-ios

ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy

ios.ios_deploy_branch = 1.12.2

ios.codesign.allowed = false


[buildozer]

# -----------------------------------------------------------------------------
# Buildozer
# -----------------------------------------------------------------------------

# 2 = saída detalhada
log_level = 2

warn_on_root = 1

# Diretórios padrão.
#
# build_dir = ./.buildozer
# bin_dir = ./bin
