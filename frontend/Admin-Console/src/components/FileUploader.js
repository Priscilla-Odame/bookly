import {useState, useEffect} from 'react';
import UploadService from "../../src/services/FileUploadservice";
import "bootstrap/dist/css/bootstrap.min.css";




 //upload file with progress bar state object
 const UploadFiles = () => {

            const [selectedFiles, setselectedFiles] = useState(undefined);
            // const [currentFile, setCurrentFile]= useState(undefined);
            const [progressInfos, setprogressInfos] = useState(0);
            const [message, setMessage] = useState("");

            const [fileInfos, setFileInfos] = useState([]);
                
            // const selectFile = (event) => {
            //     selectedFiles (event.target.files);
            // }
            const selectFiles = (e) => {
                progressInfos(e.target.files)
                setselectedFiles(e.target.files)
                console.log(e.target.files)
            }

            const upload = () =>{
                const selectedFiles = selectedFiles;

                let _progressInfos = [];
                setselectedFiles(selectedFiles);

                for (let i= 0; i< selectedFiles.length; i++){
                    _progressInfos.push({percentage: 0, fileName: selectedFiles[i].name})
                

                UploadService.upload(setselectedFiles[i], (event) => {
                    _progressInfos.push(Math.round((100 * event.loaded) / event.total))
                })
                .then((response) => {
                    setMessage("Upload successful");
                    return UploadService.getFiles();
                })
                .then((files) => {
                    setFileInfos(files.data);
                })
                .catch(() => {
                    setprogressInfos(0);
                    setMessage("Could not upload the file!");
                    setselectedFiles(undefined);
                });

                setselectedFiles(undefined);
            }}

            // useEffect(() => {
            //     UploadService.getFiles().then((response) => {
            //         setFileInfos(response.data);
            //     });
            
            // }, []);

                return (
                    <div>
                    {currentFile && (
                        <div className="progress">
                        <div
                            className="progress-bar progress-bar-info progress-bar-striped"
                            role="progressbar"
                            aria-valuenow={progress}
                            aria-valuemin="0"
                            aria-valuemax="100"
                            style={{ width: progress + "%" }}
                        >
                            {progress}%
                        </div>
                        </div>
                    )}
                
                    <label className="btn btn-default">
                        <input type="file" accept=".doc, .docx,.pdf"  id="dataupload" name="dataupload" multiple onChange={(e) => {selectFiles(e)}} />
                    </label>
                
                    <button
                        className="btn btn-success" id="dataupload-btn"
                        disabled={!selectedFiles}
                        onClick={upload}
                    >
                        Upload
                    </button>
                
                    <div className="alert alert-light" role="alert">
                        {message}
                    </div>
                
                    <div className="card">
                        <div className="card-header">List of Files</div>
                        <ul className="list-group list-group-flush">
                        {fileInfos &&
                            fileInfos.map((file, index) => (
                            <li className="list-group-item" key={index}>
                                <a href={file.url}>{file.name}</a>
                            </li>
                            ))}
                        </ul>
                    </div>
                    </div>
                );
            };
    

export default UploadFiles;