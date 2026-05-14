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
android.minapi = 24
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.sdk = /usr/local/lib/android/sdk
android.ndk = /usr/local/lib/android/sdk/ndk/27.3.13750724

[toolchain]
ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
sdk_path = /usr/local/lib/android/sdk
