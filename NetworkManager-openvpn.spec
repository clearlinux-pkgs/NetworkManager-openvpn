#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v12
# autospec commit: a5d3013
#
Name     : NetworkManager-openvpn
Version  : 1.12.0
Release  : 19
URL      : https://download.gnome.org/sources/NetworkManager-openvpn/1.12/NetworkManager-openvpn-1.12.0.tar.xz
Source0  : https://download.gnome.org/sources/NetworkManager-openvpn/1.12/NetworkManager-openvpn-1.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: NetworkManager-openvpn-data = %{version}-%{release}
Requires: NetworkManager-openvpn-lib = %{version}-%{release}
Requires: NetworkManager-openvpn-libexec = %{version}-%{release}
Requires: NetworkManager-openvpn-license = %{version}-%{release}
Requires: NetworkManager-openvpn-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : file
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk4)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnma)
BuildRequires : pkgconfig(libnma-gtk4)
BuildRequires : pkgconfig(libsecret-1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
OpenVPN support for NetworkManager
Added by Tim Niemueller http://www.niemueller.de

%package data
Summary: data components for the NetworkManager-openvpn package.
Group: Data

%description data
data components for the NetworkManager-openvpn package.


%package lib
Summary: lib components for the NetworkManager-openvpn package.
Group: Libraries
Requires: NetworkManager-openvpn-data = %{version}-%{release}
Requires: NetworkManager-openvpn-libexec = %{version}-%{release}
Requires: NetworkManager-openvpn-license = %{version}-%{release}

%description lib
lib components for the NetworkManager-openvpn package.


%package libexec
Summary: libexec components for the NetworkManager-openvpn package.
Group: Default
Requires: NetworkManager-openvpn-license = %{version}-%{release}

%description libexec
libexec components for the NetworkManager-openvpn package.


%package license
Summary: license components for the NetworkManager-openvpn package.
Group: Default

%description license
license components for the NetworkManager-openvpn package.


%package locales
Summary: locales components for the NetworkManager-openvpn package.
Group: Default

%description locales
locales components for the NetworkManager-openvpn package.


%prep
%setup -q -n NetworkManager-openvpn-1.12.0
cd %{_builddir}/NetworkManager-openvpn-1.12.0
pushd ..
cp -a NetworkManager-openvpn-1.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719586751
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --without-libnm-glib
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --without-libnm-glib
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719586751
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/NetworkManager-openvpn
cp %{_builddir}/NetworkManager-openvpn-%{version}/COPYING %{buildroot}/usr/share/package-licenses/NetworkManager-openvpn/7231584ac45906565081b89c0ca8d5fe7f738eb0 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang NetworkManager-openvpn
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/NetworkManager/VPN/nm-openvpn-service.name

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/nm-openvpn-service.conf
/usr/share/metainfo/network-manager-openvpn.metainfo.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/NetworkManager/libnm-vpn-plugin-openvpn-editor.so
/V3/usr/lib64/NetworkManager/libnm-vpn-plugin-openvpn.so
/usr/lib64/NetworkManager/libnm-vpn-plugin-openvpn-editor.so
/usr/lib64/NetworkManager/libnm-vpn-plugin-openvpn.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/nm-openvpn-auth-dialog
/V3/usr/libexec/nm-openvpn-service
/V3/usr/libexec/nm-openvpn-service-openvpn-helper
/usr/libexec/nm-openvpn-auth-dialog
/usr/libexec/nm-openvpn-service
/usr/libexec/nm-openvpn-service-openvpn-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/NetworkManager-openvpn/7231584ac45906565081b89c0ca8d5fe7f738eb0

%files locales -f NetworkManager-openvpn.lang
%defattr(-,root,root,-)

