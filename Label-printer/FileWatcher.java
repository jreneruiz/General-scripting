import java.util.*;
import java.io.*;

/**
 * 
 * FileWatcher
 * Class that are watching the specified file
 * 
 * 
 * @author jreneruiz
 * @version 1.0
 * @since 19-06-2015
 */
public abstract class FileWatcher extends TimerTask {
	
	private long timeStamp;
	private File file;
	
	/**
	 * 
	 * @param file
	 */
	public FileWatcher( File file ) {
		this.file = file;
		this.timeStamp = file.lastModified();
	}
	
	/**
	 * 
	 * Method run () overwritten to identify the last time
	 * the file was saved
	 */
	public final void run() {	
		long timeStamp = file.lastModified();
	    if( this.timeStamp != timeStamp ) {
	    	this.timeStamp = timeStamp;
	    	onChange(file);
	    }
	}

	/**
	 * 
	 * @param file 
	 */
	protected abstract void onChange( File file );
}