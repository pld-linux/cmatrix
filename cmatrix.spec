Summary:	CMatrix - show a scrolling 'Matrix' like screen in Linux (curses based)
Name:		cmatrix
Version:	1.1b
Release:	4
License:	GPL
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	http://www.asty.org/cmatrix/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
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
aclocal
autoconf
automake -a -c
CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -I%{_includedir}/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/{consolefonts,fonts/misc},%{_bindir}} \
	$RPM_BUILD_ROOT%{_mandir}/man1

install cmatrix $RPM_BUILD_ROOT%{_bindir}
install cmatrix.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mtx.pcf $RPM_BUILD_ROOT%{_datadir}/fonts/misc
install matrix.psf.gz $RPM_BUILD_ROOT%{_datadir}/consolefonts

gzip -9nf NEWS README README.fonts TODO \
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
%{_datadir}/consolefonts/*
%{_mandir}/man1/*
