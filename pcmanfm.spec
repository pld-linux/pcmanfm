Summary:	File manager for GTK
Summary(pl.UTF-8):	Zarządca plików dla GTK
Name:		pcmanfm
Version:	0.5
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	fe1a836eed6a42107e7d71a01a52f7ec
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.31
BuildRequires:	fam-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	intltool
BuildRequires:	libtool
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

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database

%postun
%update_mime_database
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.rules
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/ui
%{_datadir}/mime/packages/libmimetype.xml
%{_desktopdir}/%{name}*.desktop
%{_pixmapsdir}/%{name}.png
