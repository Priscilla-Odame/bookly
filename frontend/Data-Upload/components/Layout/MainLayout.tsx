import MainHead from "./Head";

export default function MainLayout({ children, title }) {
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
}
