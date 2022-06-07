import Vue from "vue";
import VueRouter from "vue-router";
import AuthGuard from "./utils/auth.guard";
import { adminRoot } from "./constants/config";
import { UserRole } from "./utils/auth.roles";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: `${adminRoot}/dashboards/default`
  },
  {
    path: adminRoot,
    component: () => import(/* webpackChunkName: "app" */ "./views/app"),
    redirect: `${adminRoot}/dashboards`,
    meta: { loginRequired: true },
    /*
    define with Authorization :
    meta: { loginRequired: true, roles: [UserRole.Admin, UserRole.Editor] },
    */
    children: [
      {
        path: "dashboards",
        component: () =>
          import(/* webpackChunkName: "dashboards" */ "./views/app/dashboards"),
        redirect: `${adminRoot}/dashboards/default`,
        // meta: { roles: [UserRole.Admin, UserRole.Editor] },
        children: [
          {
            path: "default",
            component: () =>
              import(
                /* webpackChunkName: "dashboards" */ "./views/app/dashboards/Default"
              )
            // meta: { roles: [UserRole.Admin] },
          }
        ]
      },
      {
        path: "pages",
        component: () =>
          import(/* webpackChunkName: "pages" */ "./views/app/pages"),
        redirect: `${adminRoot}/pages/product`,
        children: [
          {
            path: "product",
            component: () =>
              import(
                /* webpackChunkName : "product" */ "./views/app/pages/product"
              ),
            children: [
              {
                path: "image-list/:id",
                name: "resource-list",
                component: () =>
                  import(
                    /* webpackChunkName: "product" */ "./views/app/pages/product/ImageList"
                  )
              },
              {
                path: "details-alt/:id",
                component: () =>
                  import(
                    /* webpackChunkName: "product" */ "./views/app/pages/product/DetailsAlt"
                  )
              }
            ]
          },
          {
            path: "profile",
            component: () =>
              import(
                /* webpackChunkName : "profile" */ "./views/app/pages/profile"
              ),
            children: [
              {
                path: "portfolio",
                component: () =>
                  import(
                    /* webpackChunkName: "profile" */ "./views/app/pages/profile/Portfolio"
                  )
              }
            ]
          }
        ]
      },
      {
        path: "applications",
        component: () =>
          import(
            /* webpackChunkName: "applications" */ "./views/app/applications"
          ),
        children: [
          {
            path: "survey",
            component: () =>
              import(
                /* webpackChunkName: "applications" */ "./views/app/applications/Survey"
              )
          }
        ]
      }
    ]
  },
  {
    path: "/error",
    component: () => import(/* webpackChunkName: "error" */ "./views/Error")
  },
  {
    path: "/unauthorized",
    component: () =>
      import(/* webpackChunkName: "error" */ "./views/Unauthorized")
  },
  {
    path: "/user",
    component: () => import(/* webpackChunkName: "user" */ "./views/user"),
    redirect: "/user/login",
    children: [
      {
        path: "login",
        component: () =>
          import(/* webpackChunkName: "user" */ "./views/user/Login")
      },
      {
        path: "register",
        component: () =>
          import(/* webpackChunkName: "user" */ "./views/user/Register")
      }
    ]
  },
  {
    path: "*",
    component: () => import(/* webpackChunkName: "error" */ "./views/Error")
  }
];

const router = new VueRouter({
  linkActiveClass: "active",
  routes,
  mode: "history"
});
router.beforeEach(AuthGuard);
export default router;
