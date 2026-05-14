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
android.ndk = 25
android.ndk_api = 25

[buildozer]
log_level = 2
warn_on_root = 1

[toolchain]
# 使用国内镜像源加速下载
download.url.android_ndk = https://mirrors.tuna.tsinghua.edu.cn/android/repository/android-ndk-r25b-windows.zip
download.url.android_sdk = https://mirrors.tuna.tsinghua.edu.cn/android/repository/sdk-tools-windows-4333796.zip
download.url.android_ndk_version = 25b
