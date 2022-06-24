import React, { Component, useEffect } from "react";
import { Report } from "powerbi-report-component";

export default function PushInsightsReport(props) {
  // const [accessToken, setAccessToken] = useState("H4sIAAAAAAAEAB2SR66sVgAF9_KmWGoyjaU_IOdwyTCjm5xzsrx3P3le0pHq1D8_dnp3Y5r9_P1zJ1c-t-ji18OFbY7cpKUbuabRcMCXpoIatb5q8xH2Ed1kP8hDfqfSpvta7G2SMnQt2h70ODzlhFdBYufObZ1eSuEIo5tHwAxO1tm3FpKXNinscCkxEQ0tW4PLcXDkNV0VHah0EBZ54UdJs1msHGMOcvtWrRJp_Sn30xuTrfRekUtbX3jkVy2tL1GvmeW14IwWr19IiayGc0i1uB6Dl_p25qUJmo-OkGbXLalz4tRbNFlYpzaV2p8iuqy0exkibM4g8xNjqN7701FcSNq6hI58duILcgLFMnk8CjGDaMcoMa6EyV40yQedex49Ep252bF0EzIGHkBE-lmpZSFTKEC17Ul_p0Ong0YZxRueBjNhS7p4e9_VHBojIxIPMb2nST5Ee-dRBcGC2Mwlw3sFoR4Sm8j7Cma8oFjH7_QD20tlcBXddyfr4YUhu6sVNooiraHhypzTJCWJNKxn5kMq9rE-nZC9G-eAV6QdokKNG0NMc2kUeXDczqOpS_JdJlWLuojgOyQBPB6bp6lrv7bfdlf7frM57GWU4dp8g_uhl-U2nJkTwAPSuh_Dzr8aZl3nDndjVIoLrlzmhFIUyjWPbQN64q6yzm-jOJGSlszx3FOoJrzlCAWtgUTgKif__THQJvHRpOaAc0wCE6AtuUyDtVisZTTbkMZ9pe53k2_xLhP4hwXgz89fP9xyT9uo5fdvur76YNUmZDXDi4x8kOX79I-TZtSwFWBWIm_PUH0FQ66Dmg-EBNeYMnl3kNpac3ZqfDRafh0KJwLzEV3evPqCs3x19Zm3Ft29bfuR8fZgGWpZ5tarHBz7_NYgzl0AWL_7QAUNvZTv6Qj13rPjj8F8-LpDRUAKYciauhyWBpKn1eddviLBZ_2zzeSXB9aYXtgGyer9fsKz8AjNcoanGowcQ1TDi-4pI_qQ8JHEiQ8T1dG-NZv4NZEHHPuHHdqqkr8JaEqJ19LB7NcyxdrgZnPFirKoOA1B5BdJNSWME7QzsbblW6ZA0LCNKtTAtu5vQAyIRjjtvtvl1OlImQMy79keTPUKyj__a76nKl-U4Ndy933ZDnmqU84VXYSw4gSVH-Z_yq3LId32Jf_F1CEAXttwjF2xI6Qh-7vrcQi7QKkKya5Uh4HSBGeOxAALv-UGdKsC5_dBn-fZmwY4_douThKgaDGl8ZvQrWyX5R74xwd8NjqqGaBcsbPMJ_LwW4HBmR2WS32agnCfWS8qWKtzXuPQOQRtUhd-Sz8zL942st0Jb-lxwgg5D0gkI2ezSJTed8RszPx9eUQLmwgkyCYTRIgaODbVRdXXIJdWu5VxqDHKQBiKSrMV73vGYDWf80fTCv0DiZ8Dcwk-M8pCUnJV0ofPulye-3UzfLIahjcJR9_vE_ajDiCTc4jWoCJEdVCV6cm1I5oB-HpKOzYzlbDI0yenfbEttoPp8sHp1-ev5n__A50EXemuBQAA.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLU5PUlRILUNFTlRSQUwtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQiLCJlbWJlZEZlYXR1cmVzIjp7Im1vZGVybkVtYmVkIjpmYWxzZX19");
  // const [embedUrl, setEmbedUrl] = useState("https://app.powerbi.com/reportEmbed?reportId=ffd96ae6-d380-4b0a-b892-9b10c1ccb332&groupId=c01c3203-966c-4a73-a8a9-50b6f9cc8bc8&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLU5PUlRILUNFTlRSQUwtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQiLCJlbWJlZEZlYXR1cmVzIjp7Im1vZGVybkVtYmVkIjp0cnVlfX0%3d");
  // const [reportName, setReportName] = useState("Bubble Chart");
  // const [reportId, setReportId] = useState("ffd96ae6-d380-4b0a-b892-9b10c1ccb332");
  const { accessToken, embedUrl, reportId, reportName } = props;
  const alertError = e => {
    console.log("There was an error ", e);
  };

  return (
    <>
      <Report
        style={{ height: "480px", width: "67%" }}
        embedType="report"
        tokenType="Embed"
        accessToken={accessToken}
        embedUrl={embedUrl}
        embedId={reportId}
        pageName={reportName}
        reportMode="View"
        permissions="All"
        onError={e => {
          alertError(e);
        }}
      />
    </>
  );
}
