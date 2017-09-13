Summary:	A set of default configuration for LXDE
Name:		lxde-common
Version:	0.99.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.org/
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz

# OpenMandriva customization patch
#Patch101:	lxde-common-0.5.5-pcmanfm.conf.patch
Patch102:	lxde-common-0.99.2-add-mcc-to-panel.patch
Patch103:	lxde-common-0.99.2-lxpanel-customization.patch
Patch106:	lxde-common-0.99.2-autostart.patch
Patch109:	lxde-common-0.99.2-config.patch
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc

#Requires:	smproxy
Requires:	desktop-file-utils
Requires:	libnotify
Requires:	lxde-icon-theme
Requires:	lxpanel
Requires:	lxsession
Requires:	lxterminal
Requires:	notification-daemon
Requires:	openbox
#Requires:	openmandriva-lxde-config # FIXME: missing
Requires:	pcmanfm

Suggests:	xscreensaver

Requires(post):	distro-theme

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

This package provides a set of default configuration for LXDE.

%files
%doc AUTHORS COPYING README
%dir %{_sysconfdir}/xdg/lxpanel/
%dir %{_sysconfdir}/xdg/lxpanel/LXDE
%dir %{_sysconfdir}/xdg/lxpanel/LXDE/panels
%config(noreplace) %{_sysconfdir}/xdg/lxpanel/LXDE/config
%config(noreplace) %{_sysconfdir}/xdg/lxpanel/LXDE/panels/panel
%dir %{_sysconfdir}/xdg/lxsession/LXDE/
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%dir %{_sysconfdir}/xdg/pcmanfm/
%dir %{_sysconfdir}/xdg/pcmanfm/LXDE
%config(noreplace) %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%config(noreplace) %{_sysconfdir}/xdg/openbox/LXDE/menu.xml
%config(noreplace) %{_sysconfdir}/xdg/openbox/LXDE/rc.xml
%{_bindir}/startlxde
%{_bindir}/lxde-logout
%{_bindir}/openbox-lxde
%dir %{_datadir}/lxde
%{_datadir}/lxde/*
%{_datadir}/applications/lxde-logout.desktop
%{_datadir}/applications/lxde-screenlock.desktop
%{_datadir}/xsessions/LXDE.desktop
%{_mandir}/man1/startlxde.1*
%{_mandir}/man1/lxde-logout.1*
%{_mandir}/man1/openbox-lxde.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# we'll ship these files via openmandriva-lxde-config
rm -f %{buildroot}%{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf %{buildroot}%{_datadir}/lxde/openbox/rc.xml

# install this one manually, this provides the logout button on lxpanel:
install -pm 0644 lxde-logout.desktop.in %{buildroot}%{_datadir}/applications/lxde-logout.desktop

%check
#desktop-file-validate %{buildroot}%{_datadir}/applications/lxde-logout.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/lxde-screenlock.desktop

