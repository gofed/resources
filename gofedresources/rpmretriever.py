from .retriever import Retriever

class RpmRetriever(Retriever):

	def retrieve(self, product, distribution, build, rpm):
		"""Retrieve single rpm from Koji
		:param product:	os product, e.g. Fedora, CentOS
		:type  product:	str
		:param distribution:	os version, e.g. f23, centos7
		:type  distribution:	str
		:param build:	build nvr, e.g. etcd-2.2.2-1
		:type  build:	str
		:param rpm:	rpm, e.g. etcd-devel-2.2.2-4.fc24.noarch.rpm
		:type  rpm:	str
		"""

		# TODO(jchaloup): make build and rpm validation better!!!
		# TODO(jchaloup): move this code to module (i.e. build -> nvr, rpm -> arch)

		# get n,v,r from build
		parts = build.split("-")
		if len(parts) < 3:
			raise ValueError("Invalid build nvr: %s" % build)

		release = parts[-1]
		version = parts[-2]
		name = "-".join(parts[:-2])

		# get architecture
		parts = rpm.split(".")
		if len(parts) < 3:
			raise ValueError("Invalid rpm nvr.arch.(s)rpm: %s" % rpm)

		arch = parts[-2]

		# construct download url
		# https://kojipkgs.fedoraproject.org//packages/etcd/2.2.4/2.fc24/noarch/etcd-devel-2.2.4-2.fc24.noarch.rpm
		# https://kojipkgs.fedoraproject.org//packages/etcd/2.2.4/2.fc24/x86_64/etcd-unit-test-2.2.4-2.fc24.x86_64.rpm
		# https://kojipkgs.fedoraproject.org//packages/etcd/2.2.4/2.fc24/src/etcd-2.2.4-2.fc24.src.rpm
		rpm_url = "https://kojipkgs.fedoraproject.org/packages/%s/%s/%s/%s/%s" % (name, version, release, arch, rpm)

		return self._retrieveResource(rpm_url)

