%define		libfm	0.1.16
Summary:	File manager for GTK
Summary(pl.UTF-8):	Zarządca plików dla GTK
Name:		pcmanfm
Version:	0.9.9
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	f31ed6defb600f7046a456220d8efa3a
Patch0:		%{name}-werror.patch
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.31
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	intltool
BuildRequires:	libfm-devel >= %{libfm}
BuildRequires:	libtool
BuildRequires:	menu-cache-devel >= 0.3.2
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	libfm >= %{libfm}
Suggests:	gnome-icon-theme
Suggests:	lxde-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcmanfm is a fast and lightweight file manager which features tabbed
browsing and user-friendly interface.

%description -l pl.UTF-8
pcmanfm jest szybkim i lekkim zarządcą plików z przyjaznym interfejsem
użytkownika, umożliwiającym przeglądanie katalogów w zakładkach.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# see lxde-common
install -d $RPM_BUILD_ROOT/etc/xdg/pcmanfm/LXDE

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/tt_RU

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%dir /etc/xdg/pcmanfm
%dir /etc/xdg/pcmanfm/default
%dir /etc/xdg/pcmanfm/LXDE
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/pcmanfm/default/pcmanfm.conf
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui
%{_desktopdir}/%{name}*.desktop
