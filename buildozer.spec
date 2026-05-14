[app]
title = MyFirstApp
package.name = myapp
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET
android.api = 33
android.ndk = 27
android.ndk_api = 25
android.accept_sdk_license = True
android.build_tools_version = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1

[toolchain]
# 使用系统自带的 NDK（GitHub Actions 已安装 NDK 27）
ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
