%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Find every application in the system
Name:		xfce4-appfinder
Version:	4.9.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-appfinder/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	perl(XML::Parser)
BuildRequires:	garcon-devel >= 0.1.11
BuildRequires:	xfconf-devel >= 4.9.0
BuildRequires:	desktop-file-utils
Obsoletes:	xfce-appfinder

%description
Xfce appfinder is an useful software that permits you to find
every application in the system supporting Desktop entry format.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

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
