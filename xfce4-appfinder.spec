Summary:	Find every application in the system
Name:		xfce4-appfinder
Version:	4.4.2
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	xfce4-appfinder-%{version}.tar.bz2
Patch0:		%{name}-4.4.1-incremental-search.patch
Patch1:		00_enable-label-word-wrap.patch
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
Obsoletes:	xfce-appfinder
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfce appfinder is an useful software that permits you to find
every application in the system supporting Desktop entry format.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{32x32,16x16}/apps
convert src/%{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert src/%{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

desktop-file-install \
  --remove-category="Application" \
  --remove-category="X-FACE" \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/xfce4/*
%{_iconsdir}/hicolor/*/apps/*.png
