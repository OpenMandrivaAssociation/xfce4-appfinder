%define url_ver %(echo %{version} | cut -c 1-4)

Summary:	Find every application in the system
Name:		xfce4-appfinder
Version:	4.14.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-appfinder/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	git-core
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.12
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	desktop-file-utils
Obsoletes:	xfce-appfinder

%description
Xfce appfinder is an useful software that permits you to find
every application in the system supporting Desktop entry format.

%prep
%autosetup -p1 -Sgit_am

%build
#configure
NOCONFIGURE=1 xdt-autogen
%make_build

%install
%make_install

desktop-file-install \
  --remove-category="Application" \
  --remove-category="X-FACE" \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/appdata/xfce4-appfinder.appdata.xml
