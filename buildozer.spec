[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy

android.api = 33
android.ndk = 25b
android.sdk = 24
android.archs = arm64-v8a
android.minapi = 21

android.accept_sdk_license = True
android.skip_update = False
android.autofocus = True

builddir = .buildozer
bin_dir = bin
