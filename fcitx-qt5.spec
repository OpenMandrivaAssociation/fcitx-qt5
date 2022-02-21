%define major 0
%define develname %mklibname %{name} -d

Summary: Qt 5.x IM plugin for fcitx
Name: fcitx-qt5
Version:	1.2.7
Release:	1
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
Source0: http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(xkbcommon)

%description
Qt 5.x IM plugin for fcitx.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%mklibname FcitxQt5DBusAddons 1
Requires:	%mklibname FcitxQt5WidgetsAddons 1

%description -n %{develname}
Development files and headers library for %{name}.

%prep
%setup -q

%build
export CMAKE_PREFIX_PATH=%_prefix/lib/qt5/%_lib/cmake/Qt5Core:%_prefix/lib/qt5/%_lib/cmake/Qt5Gui:%_prefix/lib/qt5/%_lib/cmake/Qt5Widgets:%_prefix/lib/qt5/%_lib/cmake/Qt5DBus
%cmake_qt5
%make

%install
%makeinstall_std -C build

%find_lang %{name} --all-name

%files -f %{name}.lang
%{_libdir}/qt5/plugins/platforminputcontexts/*
%{_libdir}/fcitx/libexec/fcitx-qt5-gui-wrapper
%{_libdir}/fcitx/qt/*.so

%libpackage FcitxQt5DBusAddons 1

%libpackage FcitxQt5WidgetsAddons 1

%files -n %{develname}
%{_includedir}/FcitxQt5
%{_libdir}/lib*.so
%{_libdir}/cmake/FcitxQt5DBusAddons
%{_libdir}/cmake/FcitxQt5WidgetsAddons
