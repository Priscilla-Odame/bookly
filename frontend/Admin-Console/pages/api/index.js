export async function getServerSideProps(){

    console.log(process.env.HOST_URL)
    return {
        props: {
            hello: 'world'
        }
    }
}