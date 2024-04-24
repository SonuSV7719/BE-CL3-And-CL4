package practical_8_java_RMI;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.Map;

public interface HotelServiceInterface extends Remote {
    boolean bookRoom(String guestName, int roomNumber) throws RemoteException;
    boolean cancelBooking(String guestName) throws RemoteException;
    Map<Integer, String> showBookedRoomDetails() throws RemoteException;
    
}
