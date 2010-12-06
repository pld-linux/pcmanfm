Summary:	File manager for GTK
Summary(pl.UTF-8):	Zarządca plików dla GTK
Name:		pcmanfm
Version:	0.9.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	4a7fdc0526ed14e3293d784c0ce27dea
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
BuildRequires:	libfm-devel >= 0.1.14
BuildRequires:	libtool
BuildRequires:	menu-cache-devel >= 0.3.2
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	gnome-icon-theme
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
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui
%{_desktopdir}/%{name}*.desktop
