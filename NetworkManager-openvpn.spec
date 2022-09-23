#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : NetworkManager-openvpn
Version  : 1.10.0
Release  : 12
URL      : https://download.gnome.org/sources/NetworkManager-openvpn/1.10/NetworkManager-openvpn-1.10.0.tar.xz
Source0  : https://download.gnome.org/sources/NetworkManager-openvpn/1.10/NetworkManager-openvpn-1.10.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: NetworkManager-openvpn-data = %{version}-%{release}
Requires: NetworkManager-openvpn-lib = %{version}-%{release}
Requires: NetworkManager-openvpn-libexec = %{version}-%{release}
Requires: NetworkManager-openvpn-license = %{version}-%{release}
Requires: NetworkManager-openvpn-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
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
%setup -q -n NetworkManager-openvpn-1.10.0
cd %{_builddir}/NetworkManager-openvpn-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662486818
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --without-libnm-glib
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1662486818
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/NetworkManager-openvpn
cp %{_builddir}/NetworkManager-openvpn-%{version}/COPYING %{buildroot}/usr/share/package-licenses/NetworkManager-openvpn/7231584ac45906565081b89c0ca8d5fe7f738eb0 || :
%make_install
%find_lang NetworkManager-openvpn

%files
%defattr(-,root,root,-)
/usr/lib/NetworkManager/VPN/nm-openvpn-service.name

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/nm-openvpn-service.conf
/usr/share/metainfo/network-manager-openvpn.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/NetworkManager/libnm-vpn-plugin-openvpn-editor.so
/usr/lib64/NetworkManager/libnm-vpn-plugin-openvpn.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/nm-openvpn-auth-dialog
/usr/libexec/nm-openvpn-service
/usr/libexec/nm-openvpn-service-openvpn-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/NetworkManager-openvpn/7231584ac45906565081b89c0ca8d5fe7f738eb0

%files locales -f NetworkManager-openvpn.lang
%defattr(-,root,root,-)

