# Resource handling

**Components**
- storages
- providers
- controller

All resources are stored as tarballs or (s)rpms.

# Controllers

Resource providers are responsible for retrieving resources.
Storages are responsible for storing resources.
To connect both components together, resource controllers are introduced.
Responsibility of a controller is to make sure a given resource is available if requested.
E.g. if a resource client requests for source codes of a github project, controller ask storage for a resource.
If the resource is not stored, controller ask resource provider for the resource.
Once the resource is retrieved, it is stored to a storage.
Controller then responses with location of the requested resource.

Each resource type can have its own controller. Each controller can have more policies how to retrieve given resource. E.g.
- it can generate the tarball from a repository or retrieve it from upstream
- spec file for a given build can be retrieved from srpm or from dist-git

## GithubSourceCodeController

```vim
provide(project, repository, commit) (err, path)
```

## GithubRepositoryController

```vim
provide(project, repository) (err, path)
```

## KojiBuildController

```vim
provide(product, distribution, build) (err, path)
```

## KojiRpmBuildController

```vim
provide(product, distribution, build, nvr) (err, path)
```

## SpecFileController

```vim
provide(product, distribution, nvr) (err, path)
```

## Other info

- do we need ``KojiBuildController``? Is there any scenario for collection all rpms of a given build on the same node? If will run analysis of all rpms I would rather run all analysis in parallel on different nodes.

# Storages

Responsibility of a storage is to store a resource.
Tarball extraction or working with temporal directories/files is not.

- low level storages: directory, binary, file
- intermidiate level storages: tarball, (s)rpm
- high level storages: source code, repository

## Low level (basic) storages

### Directory storage
Basic storage that other storages can build on.
Provides low level operations for manipulation with directories.
Implicitely, all resource are stored under the same directory.
Directory trees can be supported too.
If resource ID is colon separated string of subids. Each subid is a string without `;` and `.` characters. E.g. ``"github:project:commit"`` gets stored (if set) as ``commit`` file under ``github/project`` directory.

**Responsibility**: store and retrieve a resource (into/from working directory)

```vim
store(path, ID) (err)
retrieve(ID) (err, path)
```
- path: local path to a resource
- ID: ID of a resource unique to given working directory

### File storage
Basic storage that other storages can build on.
Provides low level operations for manipulation with files.

**Responsibility**: store and retrieve a file (into/from storage)

```vim
store(path, ID) (err)
retrieve(ID) (err, path)
```
- path: local path to a resource
- ID: ID of a resource unique to given working directory

### Binary storage
Basic storage that other storages can build on.
Provides low level operations for manipulation with directories.
Resources are stored as a binary data.

**Responsibility**: store and retrieve a resource (into/from binary storage)

```vim
store(path, ID) (err)
retrieve(ID) (err, path)
```
- path: local path to a resource
- ID: ID of a resource unique to given working directory

## Intermediate storages

### Tarball storage
Various resource can be stored as a tarball.
E.g. source codes, git repositories.
Each resource type can have its own tarball storage which differs in a location
of a working directory.

**Responsibility**: store and retrieve tarballs into/from a storage

```vim
store(tarballpath, tarballID...) (err)
retrieve(tarballID...) (err, path)
```
- tarballpath: path to tarball
- tarballID: tarball ID, list of arguments uniquely specifying tarball resource

## High level storages

### GithubSourceCodeStorage

**Responsibility**: store and retrieve source codes into/from a storage

```vim
store(path, project, repo, commit) (err)
retrieve(project, repo, commit) (err, path)
```
- path: local path to source code
- project: github project name
- repo: github repository name of a given project
- commit: commit of a given project

### GitRepositoryStorage

**Responsibility**: store and retrieve github repositories into/from a storage

```vim
store(path, project, repo) (err)
retrieve(project, repo) (err, path)
```
- path: local path to repository
- project: github project name
- repo: github repository name of a given project

### UserDirectoryStorage

**Responsibility**: store and retrieve user specified directories into/from a storage

```vim
store(path) (err, ID)
retrieve(ID) (err, path)
```
- path: local path to directory
- ID: generated id of a directory

### SpecStorage

**Responsibility**: store and retrieve specs into/from a storage

```vim
store(path, product, distribution, nvr) (err)
retrieve(product, distribution, nvr) (err, path)
```
- path: local path to rpm
- product: OS product, e.g. Fedora, CentOS
- distribution: OS distribution, e.g. F22, F23
- nvr: spec nvr, e.g. etcd-2.2.4-2

### RpmStorage

**Responsibility**: store and retrieve (s)rpms into/from a storage

```vim
store(path, product, distribution, rpm, arch = "srpm") (err)
retrieve(product, distribution, rpm, arch = "srpm") (err, path)
```
- path: local path to rpm
- product: OS product, e.g. Fedora, CentOS
- distribution: OS distribution, e.g. F22, F23
- rpm: rpm nvr, e.g. etcd-2.2.4-2.fc24.src.rpm
- arch: architecture, if empty, srpm

### KojiBuildStorage

**Responsibility**: store and retrieve build into/from a storage

```vim
store(path, product, distribution, build) (err)
retrieve(product, distribution, build) (err, path)
```
- path: local path to rpm
- product: OS product, e.g. Fedora, CentOS
- distribution: OS distribution, e.g. F22, F23
- build: build nvr, e.g. etcd-2.2.4-2

### Other info

- other methods for each storage can be implemented: lookup, list, delete, garbage_collect
- even if all the high level storages are "just" wrappers above basic and middle level storages, they can provide additional functionality, e.g. different garbage collection settings, or their underlying storages can be replaced with more suitable without changing API
- storages can be used as caches on nodes too

# Providers

Responsibility of a provider is to retrieve a resource. E.g. retrieve source codes from github repository, clone a repository, download rpms, etc.

## GithubSourceCodeProvider

**Responsibility**: retrieve tarball with source codes for a given project and commit from upstream repository

**Expected output**: tarball containing source codes

```
retrieve(project, repository, commit) (err, path)
```

- project: github project
- repository: repository of a given project
- commit: commit of a given repository
- path: location of retrieved tarball

## BitbucketSourceCodeProvider

The same as ``GithubSourceCodeProvider``

## GooglecodeSourceCodeProvider

The same as ``GithubSourceCodeProvider``

Almost all the code.google.com projects have been moved to github.
This is mainly for backward compatibility.

## GithubRepositoryProvider

**Responsibility**: retrieve repository of a given upstream github project and repository

**Expected output**: tarball containing git repository

```
retrieve(project, repository) (err, path)
```

- project: github project
- repository: repository of a given project
- path: location of retrieved tarball

## BitbucketRepositoryProvider

The same as ``GithubRepositoryProvider``

## GooglecodeRepositoryProvider

The same as ``GithubRepositoryProvider``

Almost all the code.google.com projects have been moved to github.
This is mainly for backward compatibility

## KojiBuildProvider

**Responsibility**: retrieve build of a given nvr from Koji (with all its (s)rpms

**Expected output**: tarball with srpm and rpms

```
retrieve(product, distribution, build) (err, path)
```

- product: OS product, e.g. Fedora, CentOS
- distribution: OS distribution, e.g. F22, F23
- build: build nvr, e.g. etcd-2.2.4-2
