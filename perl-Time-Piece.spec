#
# _without_tests	- do not perform "make test
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Piece
Summary:	Object Oriented time objects
Summary(pl):	Obiekty czasu
Name:		perl-%{pdir}-%{pnam}
Version:	1.08
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards
compatible manner, so that using localtime/gmtime in the way
documented in perlfunc will still return what you expect.

%description -l pl
Ten modu³ zastêpuje standardowe funkcje localtime i gmtime
implementacjami zwracaj±cymi obiekty. Czyni to w sposób wstecznie
kompatybilny, wiêc u¿ywanie localtime/gmtime w sposób opisany w
perlfunc nadal bêdzie robiæ to, czego siê oczekuje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
#%dir %{perl_vendorarch}/%{pdir}/ # -- which package should be a Time/ owner?
%{perl_vendorarch}/%{pdir}/*.pm
#%dir %{perl_vendorarch}/auto/%{pdir} # -- which package should be a Time/ owner?
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.*
%{_mandir}/man3/*
