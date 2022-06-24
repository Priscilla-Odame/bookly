import { useEffect, useState } from "react";
import Link from "next/link";
import ClientOrganizationList from "../../../../components/dashboard/AdminPanel/ClientOrganization/list";
import ClientDetails from "../../../../components/dashboard/AdminPanel/ClientOrganization/OrganizationDetails";
import Admin from "../../../../components/Layout/Admin";
import { MdNavigateBefore } from 'react-icons/md'
import { API_PORT_HOSTED, ORGANIZATIONS, ORGKEY } from "../../../../config";


export default function ClientOrganization({orgId}) {
  return (
    <Admin title="Client Organization">
        <Link href="/dashboard/adminpanel">

            <a style={{marginLeft: "15.5%", fontSize: "18px", textDecoration: "none", 
                color: "#000", display: "flex", alignItems: "center", marginTop: "15px"}}>

                <MdNavigateBefore style={{fontSize: "26px" }}/>Back
            </a>
        </Link>
        <ClientDetails orgId={orgId} />
        <ClientOrganizationList orgId={orgId}/>
    </Admin>
  );
}


export async function getServerSideProps(context) {
  const { id } = context.query;
  const res = await fetch(`${API_PORT_HOSTED}/${ORGANIZATIONS}/administrator/?organization=${id}`)
  const data = await res.json();
  console.log("data", id)

  if (!data) {
    return {
      notFound: true,
    }
  }

  return {
    props: {
      // orgAdminData:  data, // will be passed to the page component as props
      orgId: id,
  }
}
}