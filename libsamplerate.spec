#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsamplerate
Version  : 0.1.9
Release  : 17
URL      : http://www.mega-nerd.com/SRC/libsamplerate-0.1.9.tar.gz
Source0  : http://www.mega-nerd.com/SRC/libsamplerate-0.1.9.tar.gz
Summary  : An audio Sample Rate Conversion library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: libsamplerate-bin = %{version}-%{release}
Requires: libsamplerate-lib = %{version}-%{release}
Requires: libsamplerate-license = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32sndfile)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(sndfile)
BuildRequires : sed
BuildRequires : util-linux

%description
This is libsamplerate, 0.1.9
libsamplerate (also known as Secret Rabbit Code) is a library for
perfroming sample rate conversion of audio data.

%package bin
Summary: bin components for the libsamplerate package.
Group: Binaries
Requires: libsamplerate-license = %{version}-%{release}

%description bin
bin components for the libsamplerate package.


%package dev
Summary: dev components for the libsamplerate package.
Group: Development
Requires: libsamplerate-lib = %{version}-%{release}
Requires: libsamplerate-bin = %{version}-%{release}
Provides: libsamplerate-devel = %{version}-%{release}
Requires: libsamplerate = %{version}-%{release}

%description dev
dev components for the libsamplerate package.


%package dev32
Summary: dev32 components for the libsamplerate package.
Group: Default
Requires: libsamplerate-lib32 = %{version}-%{release}
Requires: libsamplerate-bin = %{version}-%{release}
Requires: libsamplerate-dev = %{version}-%{release}

%description dev32
dev32 components for the libsamplerate package.


%package doc
Summary: doc components for the libsamplerate package.
Group: Documentation

%description doc
doc components for the libsamplerate package.


%package lib
Summary: lib components for the libsamplerate package.
Group: Libraries
Requires: libsamplerate-license = %{version}-%{release}

%description lib
lib components for the libsamplerate package.


%package lib32
Summary: lib32 components for the libsamplerate package.
Group: Default
Requires: libsamplerate-license = %{version}-%{release}

%description lib32
lib32 components for the libsamplerate package.


%package license
Summary: license components for the libsamplerate package.
Group: Default

%description license
license components for the libsamplerate package.


%prep
%setup -q -n libsamplerate-0.1.9
cd %{_builddir}/libsamplerate-0.1.9
pushd ..
cp -a libsamplerate-0.1.9 build32
popd
pushd ..
cp -a libsamplerate-0.1.9 buildavx2
popd
pushd ..
cp -a libsamplerate-0.1.9 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572463877
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static  --disable-fftw  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../buildavx512;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1572463877
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsamplerate
cp %{_builddir}/libsamplerate-0.1.9/COPYING %{buildroot}/usr/share/package-licenses/libsamplerate/b14ca785361a1ed431045adc8da1931eec2e3caf
cp %{_builddir}/libsamplerate-0.1.9/doc/license.html %{buildroot}/usr/share/package-licenses/libsamplerate/1ccce15748bd754a5cc4ec21982ca6f35220e847
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx512/
%make_install_avx512
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/avx512_1/sndfile-resample
/usr/bin/haswell/sndfile-resample
/usr/bin/sndfile-resample

%files dev
%defattr(-,root,root,-)
/usr/include/samplerate.h
/usr/lib64/haswell/avx512_1/libsamplerate.so
/usr/lib64/haswell/libsamplerate.so
/usr/lib64/libsamplerate.so
/usr/lib64/pkgconfig/samplerate.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsamplerate.so
/usr/lib32/pkgconfig/32samplerate.pc
/usr/lib32/pkgconfig/samplerate.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libsamplerate0-dev/html/SRC.css
/usr/share/doc/libsamplerate0-dev/html/SRC.png
/usr/share/doc/libsamplerate0-dev/html/api.html
/usr/share/doc/libsamplerate0-dev/html/api_callback.html
/usr/share/doc/libsamplerate0-dev/html/api_full.html
/usr/share/doc/libsamplerate0-dev/html/api_misc.html
/usr/share/doc/libsamplerate0-dev/html/api_simple.html
/usr/share/doc/libsamplerate0-dev/html/download.html
/usr/share/doc/libsamplerate0-dev/html/faq.html
/usr/share/doc/libsamplerate0-dev/html/history.html
/usr/share/doc/libsamplerate0-dev/html/index.html
/usr/share/doc/libsamplerate0-dev/html/license.html
/usr/share/doc/libsamplerate0-dev/html/lists.html
/usr/share/doc/libsamplerate0-dev/html/quality.html
/usr/share/doc/libsamplerate0-dev/html/win32.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libsamplerate.so.0
/usr/lib64/haswell/avx512_1/libsamplerate.so.0.1.8
/usr/lib64/haswell/libsamplerate.so.0
/usr/lib64/haswell/libsamplerate.so.0.1.8
/usr/lib64/libsamplerate.so.0
/usr/lib64/libsamplerate.so.0.1.8

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libsamplerate.so.0
/usr/lib32/libsamplerate.so.0.1.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsamplerate/1ccce15748bd754a5cc4ec21982ca6f35220e847
/usr/share/package-licenses/libsamplerate/b14ca785361a1ed431045adc8da1931eec2e3caf
