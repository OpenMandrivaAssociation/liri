%define		major	1
%define		libname	%mklibname %{oname} %{major}
%define		devname	%mklibname %{oname} -d
%define		snapshot 0

Summary:	Fast browser based on QtWebEngine
Name:		liri
Version:	0.3
%if 0%snapshot
Release:	0.%{snapshot}.1
Source0:	liri-browser-%{snapshot}.tar.xz
%else
Release:	1
Source0:	https://github.com/liri-project/liri-browser/archive/v%{version}.tar.gz
%endif
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
Group:		Networking/WWW
Url:		http://liriproject.me/browser
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5X11Extras)
Requires:	qml-material

%description
QtWebEngine based browser following the Material Design guidelines

%files
%{_bindir}/liri-browser

%prep
%if 0%{snapshot}
%setup -q -n %{name}-%{snapshot}
%else
%setup -q -n %{name}-browser-%{version}/
%endif
%apply_patches
sed -i -e 's,/opt/$${TARGET}/bin,%{_bindir},g' deployment.pri

%build
export USE_LIBPATH=%{_libdir}/
export USE_WEBGL="true"
%qmake_qt5
%make STRIP=true

%install
make install INSTALL_ROOT=%{buildroot} STRIP=true
