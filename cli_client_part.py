    def getPrefixedSize(self):
        """returns tuple (reduced folder size, corresponding prefix)"""
        prefix = [' ', 'k', 'M', 'G', 'T', 'P']
        folder_size = self._folder_size
        n = 0
        while folder_size > 1024:
            folder_size /= 1024
            n += 1
        return (folder_size, prefix[n])

    def deepFolderSize(self, isPrefix):
        """get folder size recursively, starting from current folder"""
        resp = self.api_client.metadata(self.current_path)
        if 'contents' in resp:
            for f in resp['contents']:
                if f['is_dir']:
                    self.current_path = f['path']
                    self.deepFolderSize(isPrefix)
                    self._num_folders += 1
                else:
                    self._folder_size += int(f['bytes'])
                    self._num_files += 1
        
        if isPrefix:
            #With prefix, adapts prefix (kB, MB, etc) to size
            r = self.getPrefixedSize()
            small_folder_size = round(r[0], 2)
            sys.stdout.write('%8.2f %sB, ' % (small_folder_size, r[1]))
            num_chars = len(str(small_folder_size)) + len(str(self._num_files)) + len(str(self._num_folders))
        else:
            #Without prefix, uses bytes
            sys.stdout.write('%12i B, ' % self._folder_size)
            num_chars = len(str(self._folder_size)) + len(str(self._num_files)) + len(str(self._num_folders))

        sys.stdout.write('%i files, ' % self._num_files)
        sys.stdout.write('%i folders' % self._num_folders)
        sys.stdout.write('\b' * (num_chars + 30))
        sys.stdout.flush()

    @command()
    def do_folder_size(self):
        """init counters. remember current path"""
        self._num_files = 0
        self._num_folders = 0
        self._folder_size = 0.0

        prev_path = self.current_path
        self.deepFolderSize(isPrefix=True)
        print
        self.current_path = prev_path
