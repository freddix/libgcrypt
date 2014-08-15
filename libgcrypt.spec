Summary:	Cryptographic library based on the code from GnuPG
Name:		libgcrypt
Version:	1.6.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
# Source0-md5:	a5a5060dc2f80bcac700ab0236ea47dc
Patch0:		%{name}-config.patch
URL:		http://www.gnu.org/directory/security/libgcrypt.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgpg-error-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a general purpose cryptographic library based on the code from
GnuPG. It provides functions for all cryptograhic building blocks:
symmetric ciphers (AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash
algorithms (MD5, RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all
hash algorithms), public key algorithms (RSA, ElGamal, DSA), large
integer functions, random numbers and a lot of supporting functions.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop libgcrypt applications.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS THANKS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/dumpsexp
%attr(755,root,root) %{_bindir}/hmac256
%attr(755,root,root) %{_bindir}/mpicalc
%attr(755,root,root) %ghost %{_libdir}/libgcrypt.so.??
%attr(755,root,root) %{_libdir}/libgcrypt.so.*.*.*
%{_mandir}/man1/hmac256.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgcrypt-config
%attr(755,root,root) %{_libdir}/libgcrypt.so
%{_libdir}/libgcrypt.la
%{_infodir}/*.info*
%{_includedir}/*.h
%{_aclocaldir}/*.m4

