# File: n (Python 2.2)

global abspath
import os
import stat
__all__ = [
    'normcase',
    'isabs',
    'join',
    'splitdrive',
    'split',
    'splitext',
    'basename',
    'dirname',
    'commonprefix',
    'getsize',
    'getmtime',
    'getatime',
    'islink',
    'exists',
    'isdir',
    'isfile',
    'ismount',
    'walk',
    'expanduser',
    'expandvars',
    'normpath',
    'abspath',
    'splitunc']

def normcase(s):
    return s.replace('/', '\\').lower()


def isabs(s):
    s = splitdrive(s)[1]
    if s != '':
        pass
    return s[:1] in '/\\'


def join(a, *p):
    path = a
    for b in p:
        b_wins = 0
        if path == '':
            b_wins = 1
        elif isabs(b):
            if path[1:2] != ':' or b[1:2] == ':':
                b_wins = 1
            elif len(path) > 3 and len(path) == 3 and path[-1] not in '/\\':
                b_wins = 1
            
        
        if b_wins:
            path = b
        elif path[-1] in '/\\':
            if b and b[0] in '/\\':
                path += b[1:]
            else:
                path += b
        elif path[-1] == ':':
            path += b
        elif b:
            if b[0] in '/\\':
                path += b
            else:
                path += '\\' + b
        else:
            path += '\\'
    
    return path


def splitdrive(p):
    if p[1:2] == ':':
        return (p[0:2], p[2:])
    
    return ('', p)


def splitunc(p):
    if p[1:2] == ':':
        return ('', p)
    
    firstTwo = p[0:2]
    if firstTwo == '//' or firstTwo == '\\\\':
        normp = normcase(p)
        index = normp.find('\\', 2)
        if index == -1:
            return ('', p)
        
        index = normp.find('\\', index + 1)
        if index == -1:
            index = len(p)
        
        return (p[:index], p[index:])
    
    return ('', p)


def split(p):
    (d, p) = splitdrive(p)
    i = len(p)
    while i and p[i - 1] not in '/\\':
        i = i - 1
    (head, tail) = (p[:i], p[i:])
    head2 = head
    while head2 and head2[-1] in '/\\':
        head2 = head2[:-1]
    if not head2:
        pass
    head = head
    return (d + head, tail)


def splitext(p):
    (root, ext) = ('', '')
    for c in p:
        if c in [
            '/',
            '\\']:
            (root, ext) = (root + ext + c, '')
        elif c == '.':
            if ext:
                (root, ext) = (root + ext, c)
            else:
                ext = c
        elif ext:
            ext = ext + c
        else:
            root = root + c
    
    return (root, ext)


def basename(p):
    return split(p)[1]


def dirname(p):
    return split(p)[0]


def commonprefix(m):
    if not m:
        return ''
    
    prefix = m[0]
    for item in m:
        for i in range(len(prefix)):
            if prefix[:i + 1] != item[:i + 1]:
                prefix = prefix[:i]
                if i == 0:
                    return ''
                
                break
            
        
    
    return prefix


def getsize(filename):
    st = os.stat(filename)
    return st[stat.ST_SIZE]


def getmtime(filename):
    st = os.stat(filename)
    return st[stat.ST_MTIME]


def getatime(filename):
    st = os.stat(filename)
    return st[stat.ST_ATIME]


def islink(path):
    return 0


def exists(path):
    
    try:
        st = os.stat(path)
    except os.error:
        return 0

    return 1


def isdir(path):
    
    try:
        st = os.stat(path)
    except os.error:
        return 0

    return stat.S_ISDIR(st[stat.ST_MODE])


def isfile(path):
    
    try:
        st = os.stat(path)
    except os.error:
        return 0

    return stat.S_ISREG(st[stat.ST_MODE])


def ismount(path):
    (unc, rest) = splitunc(path)
    if unc:
        return rest in ('', '/', '\\')
    
    p = splitdrive(path)[1]
    if len(p) == 1:
        pass
    return p[0] in '/\\'


def walk(top, func, arg):
    
    try:
        names = os.listdir(top)
    except os.error:
        return None

    func(arg, top, names)
    exceptions = ('.', '..')
    for name in names:
        if name not in exceptions:
            name = join(top, name)
            if isdir(name):
                walk(name, func, arg)
            
        
    


def expanduser(path):
    if path[:1] != '~':
        return path
    
    (i, n) = (1, len(path))
    while i < n and path[i] not in '/\\':
        i = i + 1
    if i == 1:
        if os.environ.has_key('HOME'):
            userhome = os.environ['HOME']
        elif not os.environ.has_key('HOMEPATH'):
            return path
        else:
            
            try:
                drive = os.environ['HOMEDRIVE']
            except KeyError:
                drive = ''

            userhome = join(drive, os.environ['HOMEPATH'])
    else:
        return path
    return userhome + path[i:]


def expandvars(path):
    if '$' not in path:
        return path
    
    import string
    varchars = string.ascii_letters + string.digits + '_-'
    res = ''
    index = 0
    pathlen = len(path)
    while index < pathlen:
        c = path[index]
        if c == "'":
            path = path[index + 1:]
            pathlen = len(path)
            
            try:
                index = path.index("'")
                res = res + "'" + path[:index + 1]
            except ValueError:
                res = res + path
                index = pathlen - 1

        elif c == '$':
            if path[index + 1:index + 2] == '$':
                res = res + c
                index = index + 1
            elif path[index + 1:index + 2] == '{':
                path = path[index + 2:]
                pathlen = len(path)
                
                try:
                    index = path.index('}')
                    var = path[:index]
                    if os.environ.has_key(var):
                        res = res + os.environ[var]
                except ValueError:
                    res = res + path
                    index = pathlen - 1

            else:
                var = ''
                index = index + 1
                c = path[index:index + 1]
                while c != '' and c in varchars:
                    var = var + c
                    index = index + 1
                    c = path[index:index + 1]
                if os.environ.has_key(var):
                    res = res + os.environ[var]
                
                if c != '':
                    res = res + c
                
        else:
            res = res + c
        index = index + 1
    return res


def normpath(path):
    path = path.replace('/', '\\')
    (prefix, path) = splitdrive(path)
    while path[:1] == '\\':
        prefix = prefix + '\\'
        path = path[1:]
    comps = path.split('\\')
    i = 0
    while i < len(comps):
        if comps[i] in ('.', ''):
            del comps[i]
        elif comps[i] == '..':
            if i > 0 and comps[i - 1] != '..':
                del comps[i - 1:i + 1]
                i -= 1
            elif i == 0 and prefix.endswith('\\'):
                del comps[i]
            else:
                i += 1
        else:
            i += 1
    if not prefix and not comps:
        comps.append('.')
    
    return prefix + '\\'.join(comps)


def abspath(path):
    global abspath
    
    try:
        _getfullpathname = _getfullpathname
        import nt
    except ImportError:
        
        def _abspath(path):
            if not isabs(path):
                path = join(os.getcwd(), path)
            
            return normpath(path)

        abspath = _abspath
        return _abspath(path)

    if path:
        
        try:
            path = _getfullpathname(path)
        except WindowsError:
            pass

    else:
        path = os.getcwd()
    return normpath(path)

realpath = abspath
