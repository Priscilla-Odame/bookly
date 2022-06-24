import MainHead from "./Head";
import withAuth from "../Auth/PrivateRoute";

const PrivateLayout = ({ children, title }) => {
  return (
    <>
      {/* import head section */}
      <MainHead title={title} />

      <div>
        <div id="page-content-wrapper">
          <div>{children}</div>
        </div>
      </div>
    </>
  );
};

export default withAuth(PrivateLayout);
