Summary:	gEdit plugins
Summary(pl):	Wtyczki dla gEdit
Name:		gedit-plugins
Version:	2.3.2
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	36facfcf62eaa90873fe8c736c29885d
URL:		http://gedit.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gedit2-devel >= 2.3.2
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtksourceview-devel >= 0.2.1
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.2.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	eel-devel >= 2.2.0
Requires:	libgnomeprintui >= 2.2.1
Requires:	gedit2 >= 2.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gEdit plugins.

%description -l pl
Wtyczki dla gEdit.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove obsoleted *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO AUTHORS
%attr(755,root,root) %{_libdir}/gedit-2/plugins/*.so*
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_datadir}/gedit-2/glade/*
%{_datadir}/gedit-2/taglist/*
