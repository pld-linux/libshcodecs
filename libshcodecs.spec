Summary:	Library for controlling SH-Mobile VPU (Video encoding/decoding)
Summary(pl.UTF-8):	Biblioteka do sterowania układem SH-Mobile VPU (kodowanie/dekodowanie obrazu)
Name:		libshcodecs
Version:	1.6.0
Release:	0.1
License:	LGPL v2+
Group:		Libraries
# trailing #/%{name}-%{version}.tar.gz is a hack for df
#Source0Download: https://oss.renesas.com/modules/document/?libshcodecs
Source0:	https://oss.renesas.com/modules/document/gate.php/?way=attach&refer=libshcodecs&openfile=%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0-md5:	53bbc87be5bb4f4a8b790a80f10f8e4d
URL:		https://oss.renesas.com/modules/document/?libshcodecs
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libshbeu-devel >= 1.0.0
BuildRequires:	libshveu-devel >= 1.6.0
BuildRequires:	libuiomux-devel >= 1.6.0
BuildRequires:	pkgconfig
#BuildRequires:	VPU middleware libraries (proprietary Renesas SDK)
Requires:	libshbeu >= 1.0.0
Requires:	libshveu >= 1.6.0
Requires:	libuiomux >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libshcodecs is a library for controlling SH-Mobile VPU (Video
encoding/decoding).

%description -l pl.UTF-8
Biblioteka do sterowania układem SH-Mobile VPU (kodowanie/dekodowanie
obrazu).

%package devel
Summary:	Header files for libshcodecs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libshcodecs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libshbeu-devel >= 1.0.0
Requires:	libshveu-devel >= 1.6.0
Requires:	libuiomux-devel >= 1.6.0

%description devel
Header files for libshcodecs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libshcodecs.

%package static
Summary:	Static libshcodecs library
Summary(pl.UTF-8):	Statyczna biblioteka libshcodecs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libshcodecs library.

%description static -l pl.UTF-8
Statyczna biblioteka libshcodecs.

%package apidocs
Summary:	libshcodecs API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libshcodecs
Group:		Documentation

%description apidocs
API and internal documentation for libshcodecs library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libshcodecs.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-beu
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig (with link patch)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libshcodecs.la
# HTML packaged in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libshcodecs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/shcodecs-cap
%attr(755,root,root) %{_bindir}/shcodecs-dec
%attr(755,root,root) %{_bindir}/shcodecs-decode-qvga-mpeg4
%attr(755,root,root) %{_bindir}/shcodecs-enc
%attr(755,root,root) %{_bindir}/shcodecs-encdec
%attr(755,root,root) %{_bindir}/shcodecs-play
%attr(755,root,root) %{_bindir}/shcodecs-record
%attr(755,root,root) %{_libdir}/libshcodecs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshcodecs.so.13
%{_datadir}/libshcodecs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshcodecs.so
%{_includedir}/shcodecs
%{_pkgconfigdir}/shcodecs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libshcodecs.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libshcodecs/html/*
