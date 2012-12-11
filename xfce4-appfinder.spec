%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Find every application in the system
Name:		xfce4-appfinder
Version:	4.10.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/xfce4-appfinder/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.9.1
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


%changelog
* Tue May 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794655
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.5-1
+ Revision: 791048
- update to new version 4.9.5

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.4-1
+ Revision: 789649
- fix file list
- update to new version 4.9.4
- reomve old stuff from spec file

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 632767
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2011.0
+ Revision: 629119
- update to new version 4.7.2

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.1-1mdv2011.0
+ Revision: 593821
- update to new version 4.7.1

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.0-1mdv2011.0
+ Revision: 579622
- update to new version 4.7.0
- adjust buildrequires

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2011.0
+ Revision: 553898
- update to new version 4.6.2

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.1
+ Revision: 543219
- rebuild for mdv 2010.1

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368574
- update to new version 4.6.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349193
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345710
- New upstream release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 334209
- update to new version 4.5.99.1

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329513
- update to new version 4.5.93

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303563
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Fri Oct 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294748
- Xfce4.6 beta1 is landing on cooker
- disable all patches
- fix file list

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-5mdv2009.0
+ Revision: 269782
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-4mdv2009.0
+ Revision: 205585
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Tue Jan 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2008.1
+ Revision: 159859
- enable label word wrap

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 110817
- correct buildrequires
- fix desktop entry
- do not package COPYING and INSTALL

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 110062
- New release 4.4.2

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - obsolete older release
    - new license policy
    - use upstream tarball name as a real name
    - use upstream name

* Wed Sep 05 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-5mdv2008.0
+ Revision: 80224
- add incremental search

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-4mdv2008.0
+ Revision: 71245
- remove X-MandrivaLinux from desktop file

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 32842
- s/imagemagick/ImageMagick
- tune up desktop file
- drop old menu style
- spec file clean

* Wed Apr 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 14739
- New release 4.4.1

