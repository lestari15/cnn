const express = require('express')
const { spawn } = require('child_process');
const app = express()

app.get('/:id/:nama', (req, res) => {


    const subprocess = runScript(req.params.id, req.params.nama);
    // print output of script
    subprocess.stdout.on('data', (data) => {
        console.log(`data:${data}`);
    });
    subprocess.stderr.on('data', (data) => {
        console.log(`error:${data}`);
    });
    subprocess.stderr.on('close', () => {
        console.log("Closed");
    });
    // const subprocess = runScript()
    res.set('Content-Type', 'text/plain');
    subprocess.stdout.pipe(res);
    subprocess.stderr.pipe(res);

})


function runScript(idKaryawan, nama) {

    var args1 = idKaryawan, args2 = nama

    return spawn('python', [
        'absensi.py', args1, args2
    ]);
}

app.listen(4000, () => console.log('Application listening on port 4000!'))