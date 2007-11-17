%define oname xfce4-appfinder
%define iconname %{oname}.png

Summary:	Find every application in the system
Name:		xfce-appfinder
Version:	4.4.1
Release:	%mkrel 5
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	xfce4-appfinder-%{version}.tar.bz2
Patch0:		%{oname}-4.4.1-incremental-search.patch
BuildRequires:	xfce-mcs-manager-devel >= %{version} 
BuildRequires:	dbh-devel 
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfce Appfinder is an useful software that permits you to find 
every application in the system supporting Desktop entry format.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11
%make

%install
rm -rf %{buildroot}
%makeinstall_std  

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{32x32,16x16}/apps
convert src/%{oname}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{iconname}
convert src/%{oname}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{iconname}

desktop-file-install \
  --remove-category="Application" \
  --remove-category="X-FACE" \
  --add-category="Filesystem" \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang xfce4-appfinder

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -n %{name} -f xfce4-appfinder.lang
%defattr(-,root,root)
%doc README ChangeLog INSTALL COPYING AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/xfce4/*
%{_iconsdir}/hicolor/*/apps/*.png
