Summary:	CMatrix - show a scrolling 'Matrix' like screen in Linux (curses based)
Name:		cmatrix
Version:	1.1b
Release:	1
License:	GPL
Group:		Utilities/Console
Group(pl):	Narzêdzia/Konsola
Source0:	http://www.asty.org/cmatrix/dist/%{name}-%{version}.tar.gz
Patch0:		cmatrix-DESTDIR.patch
URL:		http://www.asty.org/cmatrix/
BuildRequires:	ncurses-devel >= 5.0
Prereq:		/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What is CMatrix? :-)

CMatrix is a program I wrote one evening because I didn't want to have
to run Wind*ws to see the cool scrolling lines from 'The Matrix', my
fave movie. If you haven't seen this movie and you are a fan of
computers or sci-fi in general, go see this movie!!! I have seen it
twice, and I'm pondering seeing it again before it comes out on VHS.

%prep
%setup -q
%patch0 -p1

%build
automake
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Xmiscfontsdir=/usr/share/fonts/misc

gzip -9nf NEWS README README.fonts TODO \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	$RPM_BUILD_ROOT%{_datadir}/fonts/misc/*

%post
cd %{_datadir}/fonts/misc/;
/usr/X11R6/bin/mkfontdir

%postun
cd %{_datadir}/fonts/misc/;
/usr/X11R6/bin/mkfontdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fonts/misc/*
%{_mandir}/man1/*
