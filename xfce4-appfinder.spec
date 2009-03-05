Summary:	Find every application in the system
Name:		xfce4-appfinder
Version:	4.6.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4menu-devel >= %{version}
BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	thunar-devel >= 0.9.92
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
