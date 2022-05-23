package app;
import controllers.UserController;
import io.javalin.Javalin;
import repos.UserRepo;
import repos.UserRepoImpl;
import services.UserService;
import services.UserServiceImpl;

public class App {
    public static void main(String[] args) {

    Javalin app = Javalin.create(config -> config.enableCorsForAllOrigins());

    establishRoutes(app);

    app.start();

}

    private static void establishRoutes(Javalin app) {

        UserRepo ur = new UserRepoImpl();
        UserService us = new UserServiceImpl(ur);
        UserController uc = new UserController(us);

        app.get("/users", uc.getAllUsers);
        app.get("/users/:userId", uc.getUser);
        app.post("/users", uc.createUser);
        app.put("/users/:userId", uc.updateUser);
        app.delete("/users/:userId", uc.deleteUser);

    }

}

