/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2;
import com.squareup.okhttp.*;
import java.net.MalformedURLException;
import java.net.URL;

/**
 *
 * @author Rafael Antonio Morales Donis
 */
public class Practica2 {

    public static OkHttpClient clienteWeb = new OkHttpClient();
    public static inicial col = new inicial();
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*String name = "Rafal Morales";
        RequestBody formBody = new FormEncodingBuilder()
                .add("nombre", name)
                .build();
        
        String respuesta = obtenerRespuesta("metodoWeb", formBody);
        System.out.println("Saludo: "+respuesta);*/
        
        col.setVisible(true);
    }
    
    public static String obtenerRespuesta(String metodo, RequestBody formBody){
        try{
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request req = new Request.Builder().url(url).post(formBody).build();
            Response resp = clienteWeb.newCall(req).execute();
            String respuesta = resp.body().string();
            return respuesta;
        } catch(MalformedURLException ex){
            //
        }catch(Exception ex){
            //
        }
        return null;
    }
}
