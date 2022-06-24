import React from 'react'
import { useState } from 'react'
import uuid from 'react-uuid';
import Downloader from '../_user_actions/downloadService'

const useFileDownloader = () => {
    const [files, setFiles] = useState(()=>[])
    const download = file => setFiles( fileList => [ ...fileList, { ...file, downloadID: uuid() } ] );
        
    const remove = removeId => setFiles( files => [...files, filter(file => file.downloadId !== removeId)]);
    return [
        (e) => download(e),
        files.length > 0 ? <Downloader files={files} remove={e=> remove(e)}/> : null
    ]
}

export default useFileDownloader
