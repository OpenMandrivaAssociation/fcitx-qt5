%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-qt5
Version: 0.1.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Qt 5.x IM plugin for fcitx
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: qt5-devel
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(fcitx-qt)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
Qt 5.x IM plugin for fcitx.

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
export CMAKE_PREFIX_PATH=%_prefix/lib/qt5/%_lib/cmake/Qt5Core:%_prefix/lib/qt5/%_lib/cmake/Qt5Gui:%_prefix/lib/qt5/%_lib/cmake/Qt5Widgets:%_prefix/lib/qt5/%_lib/cmake/Qt5DBus
%cmake
%make

%install
%makeinstall_std -C build

%files
%_libdir/qt5/plugins/platforminputcontexts/*
%_includedir/fcitx-qt5/
%_libdir/libfcitx-qt5.*
%_libdir/pkgconfig/fcitx-qt5.pc
