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

requirements = python311,kivy,plyer

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

# NDK atualizado e compatível com o ecossistema atual
android.ndk = 27b

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
# Permissões
# -----------------------------------------------------------------------------

android.permissions =

# -----------------------------------------------------------------------------
# Ícone / Splash
# -----------------------------------------------------------------------------

# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# -----------------------------------------------------------------------------
# Outros
# -----------------------------------------------------------------------------

android.wakelock = False

android.copy_libs = 1

# -----------------------------------------------------------------------------
# iOS
# -----------------------------------------------------------------------------

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

# build_dir = ./.buildozer
# bin_dir = ./bin
