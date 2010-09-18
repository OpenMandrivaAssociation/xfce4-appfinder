%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Find every application in the system
Name:		xfce4-appfinder
Version:	4.7.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-appfinder/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel >= 4.7.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	garcon-devel >= 0.1.0
BuildRequires:	xfconf-devel >= 4.7.0
BuildRequires:	desktop-file-utils
Obsoletes:	xfce-appfinder
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfce appfinder is an useful software that permits you to find
every application in the system supporting Desktop entry format.

%prep
%setup -q

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install \
  --remove-category="Application" \
  --remove-category="X-FACE" \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/*.png
