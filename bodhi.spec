Name:           bodhi
Version:        3.1.0
Release:        3%{?dist}
BuildArch:      noarch

License:        GPLv2+
Summary:        A modular framework that facilitates publishing software updates
Group:          Applications/Internet
URL:            https://github.com/fedora-infra/bodhi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Correct-the-help-text-to-remove-spaces-betwen-builds.patch
Patch1:		bodhi-moveshelve.patch

BuildRequires:   createrepo_c
BuildRequires:   fedmsg
BuildRequires:   liberation-mono-fonts
BuildRequires:   koji
BuildRequires:   packagedb-cli
BuildRequires:   pungi
BuildRequires:   python2
BuildRequires:   python2-colander
BuildRequires:   python2-cornice < 2
BuildRequires:   python2-cornice-sphinx
BuildRequires:   python2-createrepo_c
BuildRequires:   python2-cryptography
BuildRequires:   python2-devel
BuildRequires:   python2-dnf
BuildRequires:   python2-fedora
BuildRequires:   python2-feedgen
BuildRequires:   python2-flake8
BuildRequires:   python2-iniparse
BuildRequires:   python2-jinja2
BuildRequires:   python2-koji
BuildRequires:   python2-librepo
BuildRequires:   python2-markdown
BuildRequires:   python2-mock
BuildRequires:   python2-pillow
BuildRequires:   python2-pytest
BuildRequires:   python2-pytest-cov
BuildRequires:   python2-sphinx
BuildRequires:   python2-sqlalchemy_schemadisplay
BuildRequires:   python2-virtualenv
BuildRequires:   python2-yaml

%if 0%{?fedora} >= 28
BuildRequires:   python2-alembic
BuildRequires:   python2-bugzilla
BuildRequires:   python2-openid
BuildRequires:   python2-pydns
BuildRequires:   python2-pylibravatar
BuildRequires:   python2-pyramid-fas-openid
BuildRequires:   python2-simplemediawiki
BuildRequires:   python2-urlgrabber
BuildRequires:   python2-webtest
%else
BuildRequires:   python-alembic
BuildRequires:   python-bugzilla
BuildRequires:   python-openid
BuildRequires:   python-pydns
BuildRequires:   python-pylibravatar
BuildRequires:   python-pyramid-fas-openid
BuildRequires:   python-simplemediawiki
BuildRequires:   python-urlgrabber
BuildRequires:   python-webtest
%endif

%if 0%{?fedora} >= 27
BuildRequires:   python2-progressbar
%else
BuildRequires:   python-progressbar
%endif

%if 0%{?fedora} >= 26
BuildRequires:   python2-arrow
BuildRequires:   python2-bleach
BuildRequires:   python2-click
BuildRequires:   python2-dogpile-cache
BuildRequires:   python2-kitchen
BuildRequires:   python2-pyramid
BuildRequires:   python2-pyramid-mako
BuildRequires:   python2-pyramid-tm
BuildRequires:   python2-sqlalchemy
%else
BuildRequires:   python-arrow
BuildRequires:   python-bleach
BuildRequires:   python-click
BuildRequires:   python-dogpile-cache
BuildRequires:   python-kitchen
BuildRequires:   python-pyramid
BuildRequires:   python-pyramid-mako
BuildRequires:   python-pyramid-tm
BuildRequires:   python-sqlalchemy
%endif


%description
Bodhi is a web application that facilitates the process of publishing
updates for a software distribution.

A modular piece of the Fedora Infrastructure stack
* Utilizes the Koji Buildsystem for tracking RPMs
* Creates the update repositories using Mash, which composes a repository based
  on tagged builds in Koji.


%package client
Summary: Bodhi Client
Group: Applications/Internet

Requires: filesystem
Requires: koji
Requires: python2-bodhi == %{version}-%{release}
Requires: python2-dnf
Requires: python2-fedora >= 0.9
Requires: python2-koji
Requires: python2-iniparse
Requires: python2-six

%if 0%{?fedora} >= 26
Requires:   python2-click
Requires:   python2-kitchen
%else
Requires:   python-click
Requires:   python-kitchen
%endif


%description client
Client tools for interacting with bodhi.


%package docs
Summary: Bodhi documentation
Group:   Applications/Internet


%description docs
Bodhi documentation.


%package -n python2-bodhi
Summary: Common files shared by bodhi-client and bodhi-server
Group:   Applications/Internet
%{?python_provide:%python_provide python2-bodhi}


%description -n python2-bodhi
Common files shared by bodhi-client and bodhi-server.


%package server
Summary: A modular framework that facilitates publishing software updates
Group: Applications/Internet

Requires:   bodhi-client == %{version}-%{release}
Requires:   createrepo_c
Requires:   fedmsg
Requires:   fedmsg-base
Requires:   git
Requires:   httpd
Requires:   intltool
Requires:   liberation-mono-fonts
Requires:   mod_wsgi
Requires:   packagedb-cli
Requires:   pungi
Requires:   python2-bodhi == %{version}-%{release}
Requires:   python2-colander
Requires:   python2-cornice < 2
Requires:   python2-createrepo_c
Requires:   python2-cryptography
Requires:   python2-fedora
Requires:   python2-feedgen
Requires:   python2-jinja2
Requires:   python2-librepo
Requires:   python2-markdown
Requires:   python2-pillow
Requires:   python2-psycopg2
Requires:   python2-waitress

%if 0%{?fedora} >= 28
Requires:   python2-alembic
Requires:   python2-bugzilla
Requires:   python2-libxml2
Requires:   python2-openid
Requires:   python2-pydns
Requires:   python2-pylibravatar
Requires:   python2-pyramid-fas-openid
Requires:   python2-simplemediawiki
Requires:   python2-urlgrabber
%else
Requires:   libxml2-python
Requires:   python-alembic
Requires:   python-bugzilla
Requires:   python-openid
Requires:   python-pydns
Requires:   python-pylibravatar
Requires:   python-pyramid-fas-openid
Requires:   python-simplemediawiki
Requires:   python-urlgrabber
%endif

%if 0%{?fedora} >= 27
Requires:   python2-koji
Requires:   python2-progressbar
%else
Requires:   python-progressbar
%endif

%if 0%{?fedora} >= 26
Requires:   python2-arrow
Requires:   python2-bleach
Requires:   python2-click
Requires:   python2-dogpile-cache
Requires:   python2-kitchen
Requires:   python2-pyramid
Requires:   python2-pyramid-mako
Requires:   python2-pyramid-tm
Requires:   python2-sqlalchemy
%else
Requires:   python-arrow
Requires:   python-bleach
Requires:   python-click
Requires:   python-dogpile-cache
Requires:   python-kitchen
Requires:   python-pyramid
Requires:   python-pyramid-mako
Requires:   python-pyramid-tm
Requires:   python-sqlalchemy
%endif

Provides:  bundled(aajohan-comfortaa-fonts)
Provides:  bundled(abattis-cantarell-fonts)
Provides:  bundled(bootstrap) = 3.0.1
Provides:  bundled(bootstrap) = 3.0.2
Provides:  bundled(bootstrap) = 3.1.1
Provides:  bunfled(chrissimpkins-hack-fonts)
Provides:  bundled(fedora-bootstrap) = 1.0.1
Provides:  bundled(fontawesome-fonts-web) = 4.4.0
Provides:  bundled(js-chart)
Provides:  bundled(js-excanvas)
Provides:  bundled(js-jquery)
Provides:  bundled(js-jquery) = 1.10.2
Provides:  bundled(js-messenger)
Provides:  bundled(js-moment)
Provides:  bundled(js-typeahead.js) = 1.1.1
Provides:  bundled(nodejs-flot)
Provides:  bundled(open-sans-fonts)
Provides:  bundled(xstatic-bootstrap-datepicker-common)


%description server
Bodhi is a modular framework that facilitates the process of publishing
updates for a software distribution.


%prep
%autosetup -p1 -n bodhi-%{version}

# Kill some dev deps
sed -i '/pyramid_debugtoolbar/d' setup.py
sed -i '/pyramid_debugtoolbar/d' devel/development.ini.example

# Kill this from the egg-info deps so that bodhi-server doesn't demand it.
sed -i '/click/d' setup.py

# The unit tests needs a development.ini
mv devel/development.ini.example development.ini


%build
%py2_build

make %{?_smp_mflags} -C docs html
make %{?_smp_mflags} -C docs man


%install
%py2_install

%{__mkdir_p} %{buildroot}/var/lib/bodhi
%{__mkdir_p} %{buildroot}/var/cache/bodhi
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bash_completion.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/fedmsg.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bodhi
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__mkdir_p} -m 0755 %{buildroot}/%{_localstatedir}/log/bodhi

%{__install} -m 0755 bodhi-complete.sh %{buildroot}%{_sysconfdir}/bash_completion.d
%{__install} -m 644 apache/%{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
%{__install} -m 640 production.ini %{buildroot}%{_sysconfdir}/%{name}/production.ini
%{__install} -m 640 alembic.ini %{buildroot}%{_sysconfdir}/%{name}/alembic.ini
%{__install} apache/%{name}.wsgi %{buildroot}%{_datadir}/%{name}/%{name}.wsgi

%{__install} -m 644 fedmsg.d/masher.py %{buildroot}%{_sysconfdir}/fedmsg.d/masher.py
%{__install} -m 644 fedmsg.d/bodhi.py %{buildroot}%{_sysconfdir}/fedmsg.d/bodhi.py

install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/man/*.1 %{buildroot}%{_mandir}/man1/

if [ ! -e %{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap ]; then
    # setuptools on EL 7 does not install bootstrap, so we need to symlink it
    ln -s ./bootstrap-3.1.1-fedora \
        %{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap
fi;


%check
# setuptools on EL 7 doesn't install bootstrap. This test ensures that bootstrap is present.
if [ ! -e %{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap ]; then
    echo "%{buildroot}%{python2_sitelib}/%{name}/server/static/bootstrap is missing, failing!"
    /usr/bin/false
fi;

# The tests need bodhi to be installed to pass. Let's build a virtualenv so we can install bodhi
# there.
virtualenv --system-site-packages --no-pip --never-download .test-virtualenv
.test-virtualenv/bin/python2 setup.py develop
.test-virtualenv/bin/python2 /usr/bin/py.test


%pre server
%{_sbindir}/groupadd -r %{name} &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d %{_datadir}/%{name} -M \
                     -c 'Bodhi Server' -g %{name} %{name} &>/dev/null || :


%files client
%defattr(-,root,root,-)
%license COPYING
%{_sysconfdir}/bash_completion.d/bodhi-complete.sh
%{_bindir}/bodhi
%{python2_sitelib}/%{name}/client
%{python2_sitelib}/%{name}_client-%{version}-py%{python2_version}.egg-info
%{_mandir}/man1/bodhi.1*


%files docs
%license COPYING
%doc docs/_build/html/ README.rst


%files -n python2-bodhi
%license COPYING
%dir %{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}/__init__.py*
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info


%files server
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/initialize_bodhi_db
%{_bindir}/bodhi-check-policies
%{_bindir}/bodhi-clean-old-mashes
%{_bindir}/bodhi-dequeue-stable
%{_bindir}/bodhi-expire-overrides
%{_bindir}/bodhi-approve-testing
%{_bindir}/bodhi-push
%{_bindir}/bodhi-untag-branched
%{_bindir}/bodhi-manage-releases
%config(noreplace) %{_sysconfdir}/bodhi/alembic.ini
%config(noreplace) %{_sysconfdir}/httpd/conf.d/bodhi.conf
%config(noreplace) %{_sysconfdir}/fedmsg.d/*
%dir %{_sysconfdir}/bodhi/
%{python2_sitelib}/%{name}/server
%{python2_sitelib}/%{name}_server-%{version}-py%{python2_version}.egg-info
%{_mandir}/man1/bodhi-approve-testing.1*
%{_mandir}/man1/bodhi-check-policies.1*
%{_mandir}/man1/bodhi-clean-old-mashes.1*
%{_mandir}/man1/bodhi-push.1*
%{_mandir}/man1/initialize_bodhi_db.1*
%attr(-,bodhi,root) %{_datadir}/%{name}
%attr(-,bodhi,bodhi) %config(noreplace) %{_sysconfdir}/bodhi/*
%attr(-,bodhi,root) %{_localstatedir}/log/bodhi
%attr(0775,bodhi,bodhi) %{_localstatedir}/cache/bodhi


%changelog
* Fri Jan 05 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 3.1.0-3
- Apply patch to move the shelves

* Tue Dec 12 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-2
- Correct bodhi-client's help text to show the correct syntax for multi-build
  updates (#1515766).

* Tue Oct 31 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0.
- https://github.com/fedora-infra/bodhi/releases/tag/3.1.0
- Require alembic in the server package (#1493678).

* Tue Oct 24 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 (#1506021).
- https://github.com/fedora-infra/bodhi/releases/tag/3.0.0
- Supports non-RPM artifacts (#1352587).

* Wed Oct 11 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.12.2-1
- Update to 2.12.2.
- https://github.com/fedora-infra/bodhi/releases/tag/2.12.2

* Wed Oct 11 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1.
- https://github.com/fedora-infra/bodhi/releases/tag/2.12.1

* Tue Oct 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0 (#1500515).
- https://github.com/fedora-infra/bodhi/releases/tag/2.12.0

* Fri Sep 22 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.11.0-3
- Retry auth upon captcha failures (#1494644).

* Wed Sep 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.11.0-2
- Use python2- versions on several dependencies.

* Tue Sep 19 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0 (#1493587).
- https://github.com/fedora-infra/bodhi/releases/tag/2.11.0

* Fri Sep 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.10.1-4
- The client should Require koji and python2-koji (#1488223).
- Fix Fedora < 27 to require python-progressbar.

* Tue Sep 05 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.10.1-3
- Use python2- prefixes for progressbar and pytest-cov dependencies.

* Tue Sep 05 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.10.1-2
- Bump the release to fix the upgrade path from F26.

* Tue Aug 22 2017 Jeremy Cline <jeremy@jcline.org> - 2.10.1-1
- Update to 2.10.1
- https://github.com/fedora-infra/bodhi/releases/tag/2.10.1

* Fri Aug 18 2017 Jeremy Cline <jeremy@jcline.org> - 2.10.0-1
- Update to 2.10.0
- https://github.com/fedora-infra/bodhi/releases/tag/2.10.0

* Tue Aug 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1, which fixes CVE-2017-1002152 (#1478587).
- https://github.com/fedora-infra/bodhi/releases/tag/2.9.1

* Tue Aug 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-4
- bodhi-server now depends on bodhi-client for some of its CLI tools (#1479456).

* Tue Aug 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-3
- Depend on filesystem instead of bash-completion (#1479341).

* Thu Aug 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-2
- Use python2- dependencies where appropriate.

* Wed Aug 02 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0 (#1477579).
- https://github.com/fedora-infra/bodhi/releases/tag/2.9.0
- Lexigraphically sort dependencies.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1.
- https://github.com/fedora-infra/bodhi/releases/tag/2.8.1
- Make a few of the python2- dependencies be python- again for F24-25.

* Tue Jun 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.8.0-2
- Use python2- versions of dependencies where available.
- Rearrange dependencies alphabetically.
- Drop client requirement on kitchen, since it doesn't use it.
- Drop server requirement on sphinx, since it doesn't use it.

* Tue Jun 20 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0.
- https://github.com/fedora-infra/bodhi/releases/tag/2.8.0

* Wed Jun 07 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.7.0-2
- Drop the alembic.ini symlink in /usr/share since it is not needed.

* Mon May 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0 (#1458342).
- https://github.com/fedora-infra/bodhi/releases/tag/2.7.0
- Install alembic.ini as a config file (#1451091).

* Fri May 05 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2 (#1445294).
- https://github.com/fedora-infra/bodhi/releases/tag/2.6.2

* Mon May 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1 (#1447149).
- https://github.com/fedora-infra/bodhi/releases/tag/2.6.1

* Mon Apr 17 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0.
- https://github.com/fedora-infra/bodhi/releases/tag/2.6.0

* Mon Apr 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.0-2
- Apply a patch to fix https://github.com/fedora-infra/bodhi/issues/1423
- Temporarily disable the tests since the patch causes two of them to fail, expectedly.

* Tue Mar 28 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0.
- https://github.com/fedora-infra/bodhi/releases/tag/2.5.0
- Declare all the bundled packages found in bodhi-server's static/ folder.
- Remove commented Requires and BuildRequires.

* Wed Mar 22 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-3
- Drop depenency on yum from the client (#1135681).

* Fri Mar 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-2
- Apply a patch to workaround https://github.com/fedora-infra/bodhi/issues/1343 until a true fix is
  available.

* Mon Feb 06 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0.
- Drop some unneeded globals from the top of the spec file.
- https://github.com/fedora-infra/bodhi/releases/tag/2.4.0

* Mon Feb 06 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.3-5
- Apply patches to fix repeat e-mails (#1396689).

* Mon Jan 30 2017 Jeremy Cline <jeremy@jcline.org> - 2.3.3-4
- Apply a patch that fixes one of the hotfixes applied in 2.3.3-3

* Fri Jan 13 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.3-3
- Apply four patches from git that are currently hotfixed on
  bodhi.fedoraproject.org.
- Conditionally depend on python-click or python2-click, since Fedora
  24 doesn't have python2-click.

* Sun Jan 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.3-2
- Require python2-click instead of python-click (#1411141).
- Backport a unit test patch so the tests will pass in 2017.

* Tue Nov 29 2016 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3.
- Don't define or delete the buildroot anymore.
- Add a Requires on fedmsg-base, which owns /etc/fedmsg.d for bodhi-server to put files in.

* Thu Nov 17 2016 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2.

* Mon Nov 07 2016 Dennis Gilmore <dennis@ausil.us> - 2.3.1-3
- remove the seemingly arbitary exclude of ppc and ppc64

* Thu Oct 27 2016 Randy Barlow <randy@electronsweatshop.com> - 2.3.1-2
- bodhi-server now requires python-click.

* Thu Oct 27 2016 Randy Barlow <randy@electronsweatshop.com> - 2.3.1-1
- Update to 2.3.1.

* Thu Oct 27 2016 Randy Barlow <randy@electronsweatshop.com> - 2.3.0-2
- The client and server packages now depend on the common package by release (#1389518).

* Wed Oct 19 2016 Randy Barlow <randy@electronsweatshop.com> - 2.3.0-1
- Update to 2.3.0.
- Use the fancy new py2_build and py2_install macros.
- Now depends on python-fedmsg-atomic-composer 2016.3.

* Tue Oct 04 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.4-1
- Update to 2.2.4.
- Test for presence of bootstrap rather than testing the EL version.

* Tue Sep 27 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.3-1
- Update to 2.2.3.

* Sat Sep 24 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.2-1
- Update to 2.2.2.

* Fri Sep 23 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.1-3
- Add a patch to disallow NULL text on the Comment model.

* Fri Sep 23 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.1-2
- Add a patch to skip waiting on a mash thread if there isn't one.

* Thu Sep 22 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.1-1
- Update to 2.2.1.
- Drop two patches, as they are included in 2.2.1 upstream.

* Tue Sep 20 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.0-2
- Backport two patches to correct module paths from the devel branch upstream.
- Apply a patch that stops NULL comments from being rendered with markdown.

* Mon Sep 19 2016 Randy Barlow <randy@electronsweatshop.com> - 2.2.0-1
- Update to 2.2.0. The spec file was largely taken from lmacken's COPR repository.
- Add a common subpackage to own the Python distribution (#1372461).
- Add a BuildRequires on python2-devel.
- Add a test to check for the existence of bootstrap.
- Fix some bogus dates in the changelog.
- Add a -docs subpackage and remove docs from the client and server packages.

* Tue Aug 18 2015 Luke Macken <lmacken@redhat.com> - 0.9.8-5
- Patched to work better against bodhi2 with the latest python-fedora

* Tue Sep 09 2014 Kevin Fenzi <kevin@scrye.com> 0.9.8-4
- Fix install to correct place. Fixes bug #1115136

* Fri Jun 20 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.8-3
- Only ship the client package on epel7

* Wed Feb 19 2014 Luke Macken <lmacken@redhat.com> - 0.9.8-2
- Remove the python-simplejson requirement (#1060234)

* Tue Feb 11 2014 Luke Macken <lmacken@redhat.com> - 0.9.8-1
- Update to 0.9.8

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 0.9.7-2
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Tue Sep 10 2013 Luke Macken <lmacken@redhat.com> - 0.9.7-1
- Update to 0.9.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Luke Macken <lmacken@redhat.com> - 0.9.5-2
- Update the man page

* Mon May 13 2013 Luke Macken <lmacken@redhat.com> - 0.9.5-1
- New bugfix release to work with python-bugzilla 0.8.0

* Fri Feb 22 2013 Luke Macken <lmacken@redhat.com> - 0.9.4-1
- New bugfix release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Luke Macken <lmacken@redhat.com> - 0.9.3-1
- 0.9.3 bugfix release

* Wed Aug 08 2012 Luke Macken <lmacken@redhat.com> - 0.9.2-2
- Require python-tgcaptcha2

* Sat Aug 04 2012 Luke Macken <lmacken@redhat.com> - 0.9.2-1
- 0.9.2 bugfix release

* Thu Jul 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-3
- "bodhi" now owns datadir, bodhi.cfg, and var/log/bodhi

* Thu Jul 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-2
- Fix to "bodhi" user creation.

* Thu Jul 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- Creating a 'bodhi' user for mod_wsgi

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Ralph Bean <rbean@redhat.com> - 0.8.8-1
- Sending messages with fedmsg

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Luke Macken <lmacken@redhat.com> - 0.8.5-1
- Update to the latest upstream release

* Wed Nov 16 2011 Luke Macken <lmacken@redhat.com> - 0.8.4-1
- Update to the latest upstream release

* Mon Oct 24 2011 Luke Macken <lmacken@redhat.com> - 0.8.3-1
- Update to 0.8.3

* Fri Aug 12 2011 Luke Macken <lmacken@redhat.com> - 0.8.1-1
- Update our build requirements to make the test suite happy.
- Pull in the new python-fedora-turbogears subpackage

* Thu Jun 09 2011 Luke Macken <lmacken@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Thu Mar 24 2011 Luke Macken <lmacken@redhat.com> - 0.7.15-1
- Update to 0.7.15

* Fri Mar 11 2011 Luke Macken <lmacken@redhat.com> - 0.7.14-1
- Update to 0.7.14

* Fri Mar 04 2011 Luke Macken <lmacken@redhat.com> - 0.7.13-1
- Update to 0.7.13

* Mon Feb 28 2011 Luke Macken <lmacken@redhat.com> - 0.7.12-1
- Update to 0.7.12

* Thu Feb 24 2011 Luke Macken <lmacken@redhat.com> - 0.7.11-1
- Update to 0.7.11

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Luke Macken <lmacken@redhat.com> - 0.7.10-1
- 0.7.10 release

* Mon Sep 20 2010 Luke Macken <lmacken@redhat.com> - 0.7.9-1
- 0.7.9 release

* Thu Aug 12 2010 Luke Macken <lmacken@redhat.com> - 0.7.8-1
- 0.7.8 release
- Require python-kitchen

* Wed Aug 04 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.7.7-2
- Reenable the TurboGears bits

* Tue Aug 03 2010 Luke Macken <lmacken@redhat.com> - 0.7.7-1
- 0.7.7 release

* Sat Jul 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.5-4
- A little strange, the tarball changed on us....

* Tue Jul 27 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.5-3
- Disable Requirements that are necessary for operation of hte server.  This is
  a temporary change to get the package building on python-2.7.  Need to revert
  this once the TG stack is rebuilt

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 29 2010 Luke Macken <lmacken@redhat.com> - 0.7.5-1
- 0.7.5 release

* Thu Mar 04 2010 Luke Macken <lmacken@redhat.com> - 0.7.4-1
- 0.7.4

* Thu Mar 04 2010 Luke Macken <lmacken@redhat.com> - 0.7.3-1
- 0.7.3

* Wed Mar 03 2010 Luke Macken <lmacken@redhat.com> - 0.7.2-1
- 0.7.2 bugfix release

* Tue Feb 16 2010 Luke Macken <lmacken@redhat.com> - 0.7.1-1
- Fix a regression in our metrics controller, and unvail a new
  metrics JSON API

* Tue Feb 16 2010 Luke Macken <lmacken@redhat.com> - 0.7.0-2
- Add the F13 updates-testing mash configuration

* Mon Jan 18 2010 Luke Macken <lmacken@redhat.com> - 0.7.0-1
- 0.7.0 release, prepping for the F13 release
- Critical Path & No Frozen Rawhide proposals implemented
- Many other bugfixes, enhancements, and optimizations

* Fri Nov 06 2009 Luke Macken <lmacken@redhat.com> - 0.6.12-1
- 0.6.12, for F12

* Sat Sep 19 2009 Luke Macken <lmacken@redhat.com> - 0.6.11-1
- 0.6.11

* Fri Sep 18 2009 Luke Macken <lmacken@redhat.com> - 0.6.10-1
- 0.6.10

* Thu Sep 17 2009 Luke Macken <lmacken@redhat.com> - 0.6.9-2
- More CSRF tweaks

* Thu Sep 17 2009 Luke Macken <lmacken@redhat.com> - 0.6.9-1
- 0.6.9

* Mon Sep 14 2009 Luke Macken <lmacken@redhat.com> - 0.6.8-1
- 0.6.8

* Wed Sep 09 2009 Luke Macken <lmacken@redhat.com> - 0.6.7-1
- 0.6.7

* Wed Sep 09 2009 Luke Macken <lmacken@redhat.com> - 0.6.6-1
- 0.6.6

* Wed Sep 09 2009 Luke Macken <lmacken@redhat.com> - 0.6.5-1
- 0.6.5

* Fri Aug 14 2009 Luke Macken <lmacken@redhat.com> - 0.6.4-1
- 0.6.4

* Thu Aug 13 2009 Luke Macken <lmacken@redhat.com> - 0.6.3-1
- 0.6.3

* Fri Jul 10 2009 Luke Macken <lmacken@redhat.com> - 0.6.2-1
- 0.6.2

* Thu Jul 09 2009 Luke Macken <lmacken@redhat.com> - 0.6.1-1
- 0.6.1

* Thu Jul 09 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-1
- 0.6.0 final

* Mon Jul 06 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.7.beta
- beta7

* Mon Jul 06 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.6.beta
- beta6

* Mon Jul 06 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.5.beta
- beta5, with EPEL mash configs

* Fri Jul 03 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.4.beta
- beta4

* Fri Jul 03 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.3.beta
- beta3

* Fri Jul 03 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.2.beta
- beta2
- Make our Bugzilla cookie file configurable

* Thu Jul 02 2009 Luke Macken <lmacken@redhat.com> - 0.6.0-0.1.beta
- 0.6.0 beta

* Mon Jun 22 2009 Luke Macken <lmacken@redhat.com> - 0.5.27-01
- Latest upstream release to bring in fixed mash config files.

* Fri Jun 12 2009 Luke Macken <lmacken@redhat.com> - 0.5.26-1
- Latest upstream release with a variety of fixes and pkgdb-0.4 support.

* Tue May 12 2009 Luke Macken <lmacken@redhat.com> - 0.5.25-1
- Latest upstream bugfix release to work around some TG 1.0.8
  brokenness, and make our masher a bit more robust.

* Tue May 12 2009 Luke Macken <lmacken@redhat.com> - 0.5.24-1
- 0.5.24 bugfix release

* Thu May 07 2009 Luke Macken <lmacken@redhat.com> - 0.5.23-1
- Add mash configs for F11, with deltarpm support.

* Thu Apr 30 2009 Luke Macken <lmacken@redhat.com> - 0.5.22-1
- Remove pagination patch, as Fedora Infrastructure is now TG 1.0.8

* Thu Apr 30 2009 Luke Macken <lmacken@redhat.com> - 0.5.21-1
- Update to TG 1.0.8 API (fixes a @paginate issue)

* Mon Apr 06 2009 Luke Macken <lmacken@redhat.com> - 0.5.20-1
- Fix a bug when sending mash requests through the ProxyClient
- More Python2.4 workarounds

* Mon Apr 06 2009 Luke Macken <lmacken@redhat.com> - 0.5.19-3
- Update to work with Python2.4

* Mon Apr 06 2009 Luke Macken <lmacken@redhat.com> - 0.5.19-2
- Revision bump to bring it up to speed with the fedora infra package

* Sat Mar 21 2009 Luke Macken <lmacken@redhat.com> - 0.5.19-1
- 0.5.19
- Add a patch to get pagination working in TG 1.0.4.4

* Sat Mar 14 2009 Luke Macken <lmacken@redhat.com> - 0.5.17-4
- Require httpd

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Luke Macken <lmacken@redhat.com> - 0.5.18-1
- Bugfix release, and to stop using deprecated python-fedora APIs.

* Mon Feb 2 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.17-2
- Own the %%{_sysconfdir}/bodhi directory.

* Thu Jan 22 2009 Luke Macken <lmacken@redhat.com> - 0.5.17-1
- Latest upstream bugfix release.

* Mon Jan 05 2009 Luke Macken <lmacken@redhat.com> - 0.5.16-1
- Latest upstream bugfix release.

* Mon Dec 22 2008 Luke Macken <lmacken@redhat.com> - 0.5.15-1
- Latest release, with more masher improvements.

* Fri Dec 19 2008 Luke Macken <lmacken@redhat.com> - 0.5.14-1
- Latest upstream release, containing some masher improvements.

* Wed Dec 10 2008 Luke Macken <lmacken@redhat.com> - 0.5.13-1
- Latest upstream release to fix various metrics/rss issues

* Mon Nov 24 2008 Luke Macken <lmacken@redhat.com> - 0.5.12-1
- Latest upstream release, to fix the 10k bug

* Fri Nov 21 2008 Luke Macken <lmacken@redhat.com> - 0.5.11-1
- Various F10 release tweaks

* Fri Oct 24 2008 Luke Macken <lmacken@redhat.com> - 0.5.10-3
- Latest upstream release

* Wed Oct 15 2008 Luke Macken <lmacken@redhat.com> - 0.5.9-2
- Fix a trivial module import issue

* Tue Oct 14 2008 Luke Macken <lmacken@redhat.com> - 0.5.9-1
- Fix a variety of bugs, including a race-condition when editing.

* Mon Oct 13 2008 Steve 'Ashcrow' Milner <smilner@redhat.com> - 0.5.8-2
- Added default attributes to client files.

* Sun Oct 12 2008 Luke Macken <lmacken@redhat.com> - 0.5.8-1
- Minor release to fix some new update creation bugs

* Thu Oct 09 2008 Luke Macken <lmacken@redhat.com> - 0.5.7-1
- Latest release, containing some API improvements

* Tue Oct 07 2008 Luke Macken <lmacken@redhat.com> - 0.5.6-1
- Latest upstream release.

* Mon Oct 06 2008 Luke Macken <lmacken@redhat.com> - 0.5.5-1
- Latest upstream release.

* Sat Oct 04 2008 Luke Macken <lmacken@redhat.com> - 0.5.4-2
- Make our masher extension point less obtrusive.

* Tue Sep 16 2008 Luke Macken <lmacken@redhat.com> - 0.5.4-1
- Latest upstream release, containing various bugfixes
- Make our python-fedora requirement explicit (#461518)

* Wed Sep 10 2008 Luke Macken <lmacken@redhat.com> - 0.5.3-1
- Latest upstream release

* Wed Sep 03 2008 Luke Macken <lmacken@redhat.com> - 0.5.2-2
- Add the masher deps to BuildRequires, since it now resides
  on the turbogears.extensions entry point and will be
  imported by pkg_resources at build time.

* Wed Sep 03 2008 Luke Macken <lmacken@redhat.com> - 0.5.2-1
- Latest upstream bugfix release

* Fri Aug 29 2008 Luke Macken <lmacken@redhat.com> - 0.5.1-3
- Fix some setuptools issues with our client subpackage

* Mon Aug 25 2008 Luke Macken <lmacken@redhat.com> - 0.5.1-2
- Include the egg-info in the client subpackage.

* Fri Aug 22 2008 Luke Macken <lmacken@redhat.com> - 0.5.1-1
- Latest upstream release

* Sun Jul 06 2008 Luke Macken <lmacken@redhat.com> - 0.5.0-1
- Latest upstream release

* Thu Jun 12 2008 Todd Zullinger <tmz@pobox.com> - 0.4.10-5
- update URL to point to fedorahosted.org

* Fri Apr 04 2008 Luke Macken <lmacken@redhat.com> - 0.4.10-4
- Add python-tgcaptcha to our server requirements

* Tue Feb 26 2008 Luke Macken <lmacken@redhat.com> - 0.4.10-3
- Add python-bugzilla to our server requirements

* Fri Jan 25 2008 Luke Macken <lmacken@redhat.com> - 0.4.10-2
- Add python-elixir to BuildRequires to make the new TG happy

* Fri Jan 25 2008 Luke Macken <lmacken@redhat.com> - 0.4.10-1
- 0.4.10
- Remove yum-utils requirement from bodhi-server

* Sun Jan  6 2008 Luke Macken <lmacken@redhat.com> - 0.4.9-1
- 0.4.9

* Fri Dec  7 2007 Luke Macken <lmacken@redhat.com> - 0.4.8-1
- 0.4.8

* Wed Nov 28 2007 Luke Macken <lmacken@redhat.com> - 0.4.7-1
- 0.4.7

* Tue Nov 20 2007 Luke Macken <lmacken@redhat.com> - 0.4.6-1
- 0.4.6

* Sun Nov 18 2007 Luke Macken <lmacken@redhat.com> - 0.4.5-2
- Add python-genshi to BuildRequires

* Sat Nov 17 2007 Luke Macken <lmacken@redhat.com> - 0.4.5-1
- 0.4.5

* Wed Nov 14 2007 Luke Macken <lmacken@redhat.com> - 0.4.4-1
- 0.4.4

* Mon Nov 12 2007 Luke Macken <lmacken@redhat.com> - 0.4.3-1
- 0.4.3

* Mon Nov 12 2007 Luke Macken <lmacken@redhat.com> - 0.4.2-1
- 0.4.2

* Mon Nov 12 2007 Luke Macken <lmacken@redhat.com> - 0.4.1-1
- 0.4.1

* Sun Nov 11 2007 Luke Macken <lmacken@redhat.com> - 0.4.0-1
- Lots of bodhi-client features

* Wed Nov  7 2007 Luke Macken <lmacken@redhat.com> - 0.3.3-1
- 0.3.3

* Thu Oct 18 2007 Luke Macken <lmacken@redhat.com> - 0.3.2-2
- Add TurboGears to BuildRequires
- Make some scripts executable to silence rpmlint

* Tue Oct 16 2007 Luke Macken <lmacken@redhat.com> - 0.3.2-1
- 0.3.2
- Add COPYING file
- s/python-json/python-simplejson/

* Sat Oct  6 2007 Luke Macken <lmacken@redhat.com> - 0.3.1-1
- 0.3.1

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> - 0.2.0-5
- Add python-fedora to bodhi-client Requires

* Mon Sep 17 2007 Luke Macken <lmacken@redhat.com> - 0.2.0-4
- Add python-json to bodhi-client Requires

* Sun Sep 16 2007 Luke Macken <lmacken@redhat.com> - 0.2.0-3
- Add cvs to bodhi-server Requires

* Sat Sep 15 2007 Luke Macken <lmacken@redhat.com> - 0.2.0-2
- Handle python-setuptools-devel changes in Fedora 8
- Update license to GPLv2+

* Thu Sep 13 2007 Luke Macken <lmacken@redhat.com> - 0.2.0-1
- Split spec file into client/server subpackages
