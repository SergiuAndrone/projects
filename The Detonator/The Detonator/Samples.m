//
//  Samples.m
//  The Detonator
//
//  Created by sergiuandrone on 28/11/2019.
//  Copyright © 2019 sergiuandrone. All rights reserved.
//

#import "Samples.h"
#import "SSZipArchive.h"

@implementation Samples

+(void)createDefaulLocation {
    NSError *error;
    NSString *currentUser = NSHomeDirectory();
    NSString *path = [currentUser stringByAppendingString:@"/Documents/Samples"];
    [[NSFileManager defaultManager] createDirectoryAtPath:path withIntermediateDirectories:YES attributes:nil error:&error];
}

+(NSNumber*)currentTimestamp {
    NSTimeInterval timestamp = [[NSDate date] timeIntervalSince1970];
    return ([NSNumber numberWithDouble:timestamp]);
}

+(void)runSystemCommandWithProcess:(NSString*)process withCmd:(NSString*)cmd {
    NSPipe *pipe = [NSPipe pipe];
    NSTask *task = [NSTask new];
    task.launchPath = process;
    task.arguments = @[cmd];
    task.standardOutput = pipe;
    task.standardError = pipe;

    [task launch];
    [task waitUntilExit];
}

+(void)dropBatTrojan:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;
    
    NSString *sampleName = [destination stringByAppendingString:@"/batTrojan"];
    NSString *pathtowrite = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];
    NSString *text = @"format c: /autotest";
    
    [text writeToFile:pathtowrite atomically:YES encoding:NSUTF8StringEncoding error:&error];
}

+(void)dropDialer:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle] pathForResource:@"malware.dialer" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.dialer/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropEicar:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.eicar" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.eicar/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropCleanable:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.remains.cleanable" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.remains.cleanable/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropKeylogger:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.keylogger" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.keylogger/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropSpyware:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.spyware" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.spyware/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropSmartdb:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.smartdb" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.smartdb/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropPacked:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.packed" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.packed/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropPUA:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.pua" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.pua/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropAdware:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.adware" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.adware/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropApplication:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.application" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.application/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropSuspected:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.suspected" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.suspected/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropSignedSuspected:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.signed.suspected" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.signed.suspected/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropSignedInfected:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.signed.infected" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/malware.signed.infected/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)dropMalwareEDR:(NSString*)destination {
    NSError *error;
    NSNumber *timestamp = self.currentTimestamp;

    NSString *dialerZip = [[NSBundle mainBundle]  pathForResource:@"malware.edr" ofType:@"zip"];
    NSString *sampleName = [destination stringByAppendingString:@"/EDR/"];
    NSString *destinationPath = [sampleName stringByAppendingFormat:@"%@", [timestamp stringValue]];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
}

+(void)executeRCAPocEdr:(NSString*)destination {
    NSError *error;

    NSString *dialerZip = [[NSBundle mainBundle] pathForResource:@"rca_poc1" ofType:@"zip"];
    NSString *destinationPath = [destination stringByAppendingString:@"/EDR/"];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
    
    NSString *pathToPOC = [destinationPath stringByAppendingString:@"rca_poc1"];

    [Samples runSystemCommandWithProcess:@"/usr/bin/open" withCmd:pathToPOC];
}

+(void)executePocHttpEdr:(NSString*)destination {
    NSError *error;

    NSString *dialerZip = [[NSBundle mainBundle] pathForResource:@"poc_http.py" ofType:@"zip"];
    NSString *destinationPath = [destination stringByAppendingString:@"/EDR/"];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
    
    NSString *pathToPOC = [destinationPath stringByAppendingString:@"poc_http.py"];

    [Samples runSystemCommandWithProcess:@"/usr/bin/python" withCmd:pathToPOC];
}

+(void)executeSudospawnATC:(NSString*)destination {
    NSError *error;

    NSString *dialerZip = [[NSBundle mainBundle] pathForResource:@"atc_poc_sudospawn.sh" ofType:@"zip"];
    NSString *destinationPath = [destination stringByAppendingString:@"/Midas/"];

    [SSZipArchive unzipFileAtPath:dialerZip toDestination:destinationPath overwrite:YES password:@"infected" error:&error];
    
    NSString *pathToPOC = [destinationPath stringByAppendingString:@"atc_poc_sudospawn.sh"];

    [Samples runSystemCommandWithProcess:@"/bin/sh" withCmd:pathToPOC];
}

@end
